# Generated by Django 3.2.7 on 2021-10-01 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sell', '0006_alter_product_ptype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ptype',
            field=models.CharField(choices=[('aluminium,', 'aluminium'), ('copper', 'copper'), ('stell', 'stell'), ('iron', 'iron'), ('brass', 'brass')], default='copper', max_length=50, null=True),
        ),
    ]
