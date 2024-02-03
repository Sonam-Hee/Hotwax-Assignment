from django.db import models
from encrypted_model_fields.fields import EncryptedCharField
# Create your models here.

class Party(models.Model):
    party_id = models.CharField(max_length=20, primary_key=True)
    party_enum_type_id = models.CharField(max_length=20, null=True, blank=True)

class Person(models.Model):
    party = models.OneToOneField(Party, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    marital_status_enum_id = models.CharField(max_length=20, null=True, blank=True)
    employment_status_enum_id = models.CharField(max_length=20, null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)

class Product(models.Model):
    product_id = models.CharField(max_length=20, primary_key=True)
    party = models.ForeignKey(Party, on_delete=models.CASCADE, null=True, blank=True)
    product_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    charge_shipping = models.CharField(max_length=1, null=True, blank=True)
    returnable = models.CharField(max_length=1, null=True, blank=True)

class OrderHeader(models.Model):
    order_id = models.CharField(max_length=20, primary_key=True)
    order_name = models.CharField(max_length=255, null=True, blank=True)
    placed_date = models.DateTimeField(null=True, blank=True)
    approved_date = models.DateTimeField(null=True, blank=True)
    status_id = models.CharField(max_length=20, null=True, blank=True)
    party = models.ForeignKey(Party, on_delete=models.CASCADE, null=True, blank=True)
    currency_uom_id = models.CharField(max_length=20, null=True, blank=True)
    product_store_id = models.CharField(max_length=20, null=True, blank=True)
    sales_channel_enum_id = models.CharField(max_length=20, null=True, blank=True)
    grand_total = models.DecimalField(max_digits=24, decimal_places=4, null=True, blank=True)
    completed_date = models.DateTimeField(null=True, blank=True)
    credit_card = EncryptedCharField(max_length=20, null=True, blank=True)

class OrderItem(models.Model):
    order_id = models.CharField(max_length=20)
    order_item_seq_id = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    item_description = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.DecimalField(max_digits=24, decimal_places=4, null=True, blank=True)
    unit_amount = models.DecimalField(max_digits=24, decimal_places=4, null=True, blank=True)
    item_type_enum_id = models.CharField(max_length=20, null=True, blank=True)

    


