# Generated by Django 4.1.6 on 2023-03-20 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ss', '0030_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]