from django.db import models

class ConsumerDetailsModel(models.Model):
    consumer_id = models.IntegerField(primary_key=True)
    consumer_name = models.CharField(max_length=30)
    consumer_contact_no = models.IntegerField(unique=True)
    consumer_email = models.EmailField(unique=True)
    consumer_password = models.CharField(max_length=10)
    consumer_address = models.TextField()
    consumer_status = models.CharField(max_length=10)
