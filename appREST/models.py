from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.exceptions import ValidationError

class Product(models.Model):
    '''Produto da empresa'''

    product =       models.CharField(max_length=50)
    price =         models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    description =   models.CharField(max_length=100)

    class Meta:
        verbose_name = "Product"

    def __str__(self):
        return self.product

    @property
    def name(self):
        return self.product.replace("_", " ").title()


def myUnique(value):
    transaction_ids = Payment.objects.values_list('transaction_id', flat=True)
    if value in transaction_ids:
        raise ValidationError("Já existe uma transação com esse ID. Experimente usar: {}.".format(max(transaction_ids)+1))

class Payment(models.Model):
    '''Pagamento da empresa'''

    PAYMENT_TYPE_CHOICES = (
        ('CT', 'Cartao'),
        ('BL', 'Boleto')
    )

    payment_date =      models.DateField()
    payment_type =      models.CharField(max_length=2, choices=PAYMENT_TYPE_CHOICES)
    product =           models.ForeignKey(Product)
    product_price =     models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    discount =          models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0')),
                                                                                    MaxValueValidator(Decimal('50.00'))])
    transaction_id =    models.PositiveIntegerField(validators=[myUnique])

    #product_price deve ser armazenado, pois o valor do produto pode mudar
    # (e aqui devemos guardar o valor da época da compra)

    #Price não precisam ser armazenados no banco de dados,
    #podendo ser derivados de outros campos.
    #Por isso são representados como propriedades.

    @property
    def price(self):
        return Decimal(self.product_price * (1-(self.discount/100)))

    class Meta:
        verbose_name = "Payment"

    def __str__(self):
        return str(self.transaction_id) + " | " + str(self.payment_date) + " | " + str(self.product)