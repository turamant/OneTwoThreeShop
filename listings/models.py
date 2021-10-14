from django.db import models

# Create your models here.

class Size(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Sex(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Modelka(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.ForeignKey(Modelka, on_delete=models.CASCADE, related_name='products',
                              default=None)
    poster = models.ImageField(upload_to='posters/%y/%m/%d', default=None)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, related_name='products')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='products')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    description = models.TextField(default=True, blank=True)

    def __str__(self):
        return f"{self.name}: {self.model.name}"

class ImageProduct(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    img = models.ImageField(upload_to='img/%y/%m%d')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='imageproducts')

    def __str__(self):
        return self.name