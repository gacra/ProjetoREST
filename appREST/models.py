from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import datetime

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
    PAYMENT_TYPE_CHOICES = (
        ('CT', 'Cartao'),
        ('BL', 'Boleto')
    )

    payment_date =  models.DateTimeField(auto_now_add=True)
    payment_type =  models.CharField(max_length=2, choices=PAYMENT_TYPE_CHOICES, default='CT')
    product =       models.ForeignKey(Product)
    product_price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    discount =      models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.01')),
                                                                                    MaxValueValidator(Decimal('50.00'))])
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    transaction_id = models.PositiveIntegerField(unique=True)

    class Meta:
        verbose_name = "Payment"

    def __str__(self):
        return str(self.transaction_id) + " | " + str(self.product) + " | " + str(self.price)