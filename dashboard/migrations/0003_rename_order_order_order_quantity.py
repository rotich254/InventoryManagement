# Generated by Django 4.2.1 on 2023-08-12 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_product_category_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order',
            new_name='order_quantity',
        ),
    ]
