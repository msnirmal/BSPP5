from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


def product_list(request):
    
    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "Enter a search criteria")
                return redirect(reverse('products'))
            products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    } 

    return render(request, 'products/products.html', context)   

def product_detail(request, product_id):

    """ A view to show individual product page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }    

    return render(request, 'products/product_detail.html', context)

def add_product(request):
    """ Add a product to the store """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)



