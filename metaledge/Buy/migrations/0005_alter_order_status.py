# Generated by Django 3.2.7 on 2021-10-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buy', '0004_auto_20211005_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('conplete', 'complete'), ('dispatched', 'dispatched'), ('confirmed', 'confirmed'), ('placed', 'placed')], default='placed', max_length=50, null=True),
        ),
    ]
