# Generated by Django 4.1.3 on 2022-12-03 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_alter_shippingaddress_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
    ]
