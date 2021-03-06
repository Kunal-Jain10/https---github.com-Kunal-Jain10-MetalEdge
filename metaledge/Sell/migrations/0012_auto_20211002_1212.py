# Generated by Django 3.2.7 on 2021-10-02 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0007_alter_seller_user'),
        ('Sell', '0011_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Account.seller'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('copper', 'copper'), ('stell', 'stell'), ('aluminium,', 'aluminium'), ('iron', 'iron'), ('brass', 'brass')], default='copper', max_length=50, null=True),
        ),
    ]
