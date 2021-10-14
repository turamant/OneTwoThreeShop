from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
from django.urls import reverse


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

    def get_absolute_url(self):
        return reverse('listings:product_list_by_category',
                       args=[self.slug]
                       )


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
    model = models.ForeignKey(Modelka, on_delete=models.CASCADE, related_name='product',
                              default=None)
    poster = models.ImageField(upload_to='posters/%y/%m/%d', default=None)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, related_name='product')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='product')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='product')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    description = models.TextField(default=True, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}: {self.model.name}"

    class Meta:
        ordering = ('-name',)
        verbose_name_plural = 'Товары'


    def get_absolute_url(self):
        return reverse(
            'listings:product_detail',
            args=[self.category.slug, self.slug]
        )

    def get_average_review_score(self):
        average_score = 0.0

        if self.reviews.count() > 0:
            total_score = sum([review.rating for review in self.reviews.all()])
        average_score = total_score / self.reviews.count()
        return round(average_score, 1)

class ImageProduct(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    img = models.ImageField(upload_to='img/%y/%m%d')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='imageproducts')

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews',
                                on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
