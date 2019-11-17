# Generated by Django 2.2.7 on 2019-11-08 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MerchantModal',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('merchant_name', models.CharField(max_length=50)),
                ('merchant_contact', models.IntegerField(unique=True)),
                ('merchant_email', models.EmailField(max_length=254, unique=True)),
                ('merchant_password', models.CharField(max_length=20)),
            ],
        ),
    ]
