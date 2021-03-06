# Generated by Django 3.2.7 on 2021-10-05 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sell', '0017_alter_product_type'),
        ('Account', '0007_alter_seller_user'),
        ('Buy', '0003_auto_20211005_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='invoice',
            field=models.FileField(blank=True, null=True, upload_to='docOrder/'),
        ),
        migrations.AlterField(
            model_name='order',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='Account.buyer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='Sell.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='Account.seller'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('placed', 'placed'), ('conplete', 'complete'), ('confirmed', 'confirmed'), ('dispatched', 'dispatched')], default='placed', max_length=50, null=True),
        ),
    ]
