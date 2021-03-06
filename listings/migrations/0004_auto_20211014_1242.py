# Generated by Django 3.2.8 on 2021-10-14 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20211014_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='poster',
            field=models.ImageField(default=None, upload_to='posters/%y/%m/%d'),
        ),
        migrations.CreateModel(
            name='ImageProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('img', models.ImageField(upload_to='img/%y/%m%d')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imageproducts', to='listings.product')),
            ],
        ),
    ]
