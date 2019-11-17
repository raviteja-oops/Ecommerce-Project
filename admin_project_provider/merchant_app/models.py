from django.db import models
from admin_app.models import MerchantModal

class ProductDetailsModal(models.Model):
    p_no = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=100,unique=True)
    p_price = models.IntegerField()
    p_quantity = models.IntegerField()
    merchant_id = models.ForeignKey(MerchantModal,on_delete=models.CASCADE)