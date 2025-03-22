# Generated by Django 5.1.7 on 2025-03-16 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_address_zip'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='customers',
            index=models.Index(fields=['last_name', 'first_name'], name='store_custo_last_na_e6a359_idx'),
        ),
        migrations.AlterModelTable(
            name='customers',
            table='store_customers',
        ),
    ]
