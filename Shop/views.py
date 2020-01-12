from django.shortcuts import render, get_object_or_404
from .models import Category, Product

from Cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.filter(available=True)

    return render(request, 'shop/product_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, product_slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=product_slug,
                                available=True)

    cart_product_form = CartAddProductForm()

    return render(request,
                  'shop/product_detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
