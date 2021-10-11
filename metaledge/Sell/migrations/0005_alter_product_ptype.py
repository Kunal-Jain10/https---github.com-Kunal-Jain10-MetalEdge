# Generated by Django 3.2.7 on 2021-10-01 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sell', '0004_alter_product_ptype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ptype',
            field=models.CharField(choices=[('stell', 'stell'), ('iron', 'iron'), ('aluminium,', 'aluminium'), ('copper', 'copper'), ('brass', 'brass')], default='copper', max_length=50, null=True),
        ),
    ]