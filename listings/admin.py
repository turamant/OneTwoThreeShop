from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from listings.models import Size, Category, Sex, Color, Product, Modelka, ImageProduct


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Sex)
class SexAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Modelka)
class ModelkaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ImageProduct)
class IamgeProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image', 'product')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.img.url} width="50" height="60"')

    get_image.short_description = "Изображение"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image', 'category', 'model', 'sex', 'color', 'size', 'price', 'count')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name', 'model')}
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50" height="60"')

    get_image.short_description = "Изображение"