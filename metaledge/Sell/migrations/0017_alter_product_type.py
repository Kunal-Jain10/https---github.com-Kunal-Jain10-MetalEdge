# Generated by Django 3.2.7 on 2021-10-05 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sell', '0016_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('brass', 'brass'), ('aluminium,', 'aluminium'), ('iron', 'iron'), ('stell', 'stell'), ('copper', 'copper')], default='copper', max_length=50, null=True),
        ),
    ]