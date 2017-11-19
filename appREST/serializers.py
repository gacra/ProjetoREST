from _decimal import Decimal
from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Product, Payment


class ProductSerializer(serializers.ModelSerializer):
    '''Serializer para o modelo do Produto'''

    class Meta:
        model = Product
        fields = ('name', 'id', 'product', 'price', 'description')


class PaymentSerializer(serializers.ModelSerializer):
    '''Serializer para o modelo do Pagamento'''

    errors_msgs = {
        'invalid': 'Formato inválido para data. Use o formato: AAAA-MM-DD.',
        'required': 'Este campo é obrigatório'
    }

    product_price = serializers.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    price = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)
    payment_date = serializers.DateField(error_messages=errors_msgs)

    class Meta:
        model = Payment
        fields = ('payment_date', 'payment_type', 'product', 'product_price', 'discount', 'price', 'transaction_id')

    #Validação extra para que o campo price seja igual ao preço do produto
    def validate(self, attrs):
        if attrs['product'].price != attrs['product_price']:
            raise serializers.ValidationError({'product_price':'Campo price deve ser igual ao preço do produto (Dica: {}).'.format(attrs['product'].price)})
        return attrs

    #Criação de novo pagamento
    def create(self, validated_data):

        payment = Payment.objects.create(
            payment_date = validated_data['payment_date'],
            payment_type = validated_data['payment_type'],
            product = validated_data['product'],
            product_price = validated_data['product_price'],
            discount = validated_data['discount'],
            transaction_id = validated_data['transaction_id']
        )

        return  payment