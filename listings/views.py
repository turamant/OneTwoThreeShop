from django.http import HttpRequest, QueryDict, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from cart.forms import CartAddProductForm
from listings.forms import ReviewForm
from listings.models import Modelka, Category, Product, Sex, Color, Size, Review


def product_list(request, category_slug=None):
    models = Modelka.objects.all()
    categories = Category.objects.all()
    sexs = Sex.objects.all()
    colors = Color.objects.all()

    sizes = Size.objects.all()
    print("Site: ", HttpRequest.get_port(request))
    print("Path: ", HttpRequest.get_full_path(request))
    print(" absolut path: ", HttpRequest.build_absolute_uri(request, location=None))
    print("///", HttpRequest.is_secure(request))
    print("Response: ", HttpResponse.content)

    if category_slug:
        requested_category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=requested_category)
        print("yes category", request.headers.get('User-Agent'))
        #print("Cocie: ", request.get_signed_cookie('name'))
        if request.user.is_authenticated:
            print("User")
        else:
            print("Not user")
    else:
        requested_category = None
        products = Product.objects.all()
        print('Not category', request.headers)
    return render(
        request,
        'product/list.html',
        {
            'models': models,
            'categories': categories,
            'sexs': sexs,
            'colors': colors,
            'sizes': sizes,
            'products': products,
            'requested_category': requested_category,
        }
    )


def product_detail(request, category_slug, product_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(
        Product,
        category_id = category.id,
        slug=product_slug
    )
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            cf = review_form.cleaned_data
            author_name = "Anonymous"
            Review.objects.create(
                product=product,
                author=author_name,
                rating=cf['rating'],
                text=cf['text']
            )

        return redirect(
            'listings:product_detail',
            category_slug=category_slug, product_slug=product_slug)
    else:
        review_form = ReviewForm()
        cart_product_form = CartAddProductForm()

    return render(
        request, 'product/detail.html',
        {
            'product': product,
            'review_form': review_form,
            'cart_production_form': cart_product_form,
        }
    )