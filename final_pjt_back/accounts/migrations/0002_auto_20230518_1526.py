# Generated by Django 3.2.18 on 2023-05-18 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20230518_1234'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='financial_products',
        ),
        migrations.AddField(
            model_name='user',
            name='registered_products',
            field=models.ManyToManyField(blank=True, null=True, related_name='registered_users', to='products.SavingProducts'),
        ),
        migrations.DeleteModel(
            name='RegisteredProduct',
        ),
    ]