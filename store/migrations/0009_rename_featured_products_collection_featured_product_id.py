# Generated by Django 5.1.7 on 2025-03-16 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20250316_1607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='featured_products',
            new_name='featured_product_id',
        ),
    ]
