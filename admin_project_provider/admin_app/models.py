from django.db import models

class MerchantModal (models.Model):
    id = models.IntegerField(primary_key=True)
    merchant_name = models.CharField(max_length=50)
    merchant_contact = models.IntegerField(unique=True)
    merchant_email = models.EmailField(unique=True)
    merchant_password = models.CharField(max_length=20)
