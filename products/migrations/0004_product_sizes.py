# Generated by Django 4.2.10 on 2024-03-02 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_is_sales_product_sales_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]