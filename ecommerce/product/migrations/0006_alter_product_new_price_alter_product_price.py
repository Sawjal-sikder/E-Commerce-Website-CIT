# Generated by Django 5.0.6 on 2024-07-01 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_new_price_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='new_price',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
    ]
