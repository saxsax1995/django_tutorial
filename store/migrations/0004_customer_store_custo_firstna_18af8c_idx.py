# Generated by Django 4.1.6 on 2023-02-21 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_slug'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['firstname', 'lastname'], name='store_custo_firstna_18af8c_idx'),
        ),
    ]
