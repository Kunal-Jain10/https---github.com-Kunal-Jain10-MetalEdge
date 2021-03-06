# Generated by Django 3.2.7 on 2021-09-30 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0005_auto_20210930_0819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50, null=True)),
                ('ptype', models.CharField(max_length=50, null=True)),
                ('pdesc', models.CharField(max_length=300, null=True)),
                ('price', models.IntegerField(null=True)),
                ('seller', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Account.seller')),
            ],
        ),
    ]
