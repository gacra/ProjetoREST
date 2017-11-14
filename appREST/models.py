from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Product(models.Model):
    '''Produto da empresa'''

    product =       models.CharField(max_length=50)
    price =         models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    description =   models.CharField(max_length=100)

    class Meta:
        verbose_name = "Product"

    def __str__(self):
        return self.product


class Payment(models.Model):
    '''Pagamento da empresa'''

    PAYMENT_TYPE_CHOICES = (
        ('CT', 'Cartao'),
        ('BL', 'Boleto')
    )

    payment_date =      models.DateField()
    payment_type =      models.CharField(max_length=2, choices=PAYMENT_TYPE_CHOICES)
    product =           models.ForeignKey(Product)
    discount =          models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.01')),
                                                                                    MaxValueValidator(Decimal('50.00'))])
    transaction_id =    models.PositiveIntegerField(unique=True)

    #product_price e price não precisam ser armazenados no banco de dados,
    #podendo ser derivados de outros campos.
    #Por isso são representados como propriedades.

    @property
    def product_price(self):
        return self.product.price

    @property
    def price(self):
        return Decimal(self.product.price * (1-(self.discount/100)))

    class Meta:
        verbose_name = "Payment"

    def __str__(self):
        return str(self.transaction_id) + " | " + str(self.payment_date) + " | " + str(self.product)