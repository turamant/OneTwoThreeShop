# Generated by Django 3.2.8 on 2021-10-14 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_product_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-name',)},
        ),
    ]