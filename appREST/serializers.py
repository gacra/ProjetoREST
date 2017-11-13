from rest_framework import serializers
from .models import Product, Payment

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('product', 'price', 'description')

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ( 'payment_date', 'payment_type', 'product', 'product_price', 'discount', 'price', 'transaction_id')
        read_only_fields = ( 'payment_date', 'price' )

    def validate(self, attrs):
        if attrs['product'].price != attrs['product_price']:
            raise serializers.ValidationError({'product_price':'Campo price deve ser igual ao preço do produto.'})
        return attrs

    def create(self, validated_data):
        product_price = validated_data['product_price']
        discount = validated_data['discount']

        payment = Payment.objects.create(
            payment_type = validated_data['payment_type'],
            product = validated_data['product'],
            product_price = product_price,
            discount = discount,
            price = product_price * (1-(discount/100)),
            transaction_id = validated_data['transaction_id']
        )

        return  payment