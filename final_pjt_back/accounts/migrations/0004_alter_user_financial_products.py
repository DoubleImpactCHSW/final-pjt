# Generated by Django 3.2.18 on 2023-05-18 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20230518_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='financial_products',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]