# Generated by Django 4.1.6 on 2023-03-20 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ss', '0033_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ss.payment'),
            preserve_default=False,
        ),
    ]
