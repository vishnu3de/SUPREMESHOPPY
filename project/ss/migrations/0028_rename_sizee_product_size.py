# Generated by Django 4.1.6 on 2023-03-20 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ss', '0027_remove_product_size_product_sizee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sizee',
            new_name='size',
        ),
    ]