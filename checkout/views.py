from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is no item in your bag")
        return redirect(reverse('products'))
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K8T7qColqL17O9lyGsIu1WuLv9yChkCWmuEsiQJu6q1wGDORXMnudGWgLfqQZJIkBplx33q8BvnHaAbTfs5ummb00Vq1pkgQr',
        'client_secret': 'test client secret',
    }


    return render(request, template, context)
