# Generated by Django 5.0.6 on 2024-07-01 11:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_is_featured_product_is_new_added_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('thumbnail', models.ImageField(upload_to='brand_thumbnails/')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='category_banners/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='category_thumbnails/'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='subcategory_banners/'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='subcategory_thumbnails/'),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='product.brand'),
        ),
    ]