from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
            'order_form': order_form,
            'stripe_public_key': 'pk_test_51PSJTC08X2T9W10k1hphlHMcFHdkYCE3pHsMyfFzgo4ZQ21h7OdBNS5gTEJAcAR9qAMbXs6ggEA6iotk23Q5M23i00J8iHKPwm',
            'client_secret': 'test client secret',
    }

    return render(request, template, context)


        
