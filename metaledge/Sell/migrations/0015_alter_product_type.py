# Generated by Django 3.2.7 on 2021-10-05 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sell', '0014_auto_20211002_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('brass', 'brass'), ('aluminium,', 'aluminium'), ('iron', 'iron'), ('copper', 'copper'), ('stell', 'stell')], default='copper', max_length=50, null=True),
        ),
    ]