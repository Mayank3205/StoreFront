# Generated by Django 5.1.7 on 2025-03-16 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_rename_customers_customer_and_more'),
    ]

    operations = [
        migrations.RunSQL("""
        INSERT INTO store_collection (title)
        VALUES ('collection1')
    ""","""
        DELETE FROM store_collection
        where title='collection1'
    """)
    ]
