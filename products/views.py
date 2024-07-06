from django.shortcuts import render

from .models import Category, Product

def categories(request):
    return {
        'categories': Category.objects.all()
    }


def product_list(request):
    products = Product.objects.all()
    
    context = {
        'products': products,
    } 

    return render(request, 'products/products.html')   



