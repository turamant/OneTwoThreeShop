# Generated by Django 3.2.8 on 2021-10-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageproduct',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]