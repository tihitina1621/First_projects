# Generated by Django 5.1.1 on 2024-09-30 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock_quantity',
            field=models.IntegerField(),
        ),
    ]
