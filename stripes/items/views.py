import stripe

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Item, Order
from .utils import build_line_items
from stripes.settings import STRIPE_KEY_SECRET, STRIPE_KEY_PUBLIC

stripe.api_key = STRIPE_KEY_SECRET


def item_detail(request, id):
    item = get_object_or_404(Item, pk=id)
    context = {
        'item': item,
        'stripe_key_public': STRIPE_KEY_PUBLIC
    }
    return render(request, 'item.html', context)


def order_detail(request, id):
    order = get_object_or_404(Order, pk=id)
    items = order.items.all()
    context = {
        'order': order,
        'items': items,
        'stripe_key_public': STRIPE_KEY_PUBLIC
    }
    return render(request, 'order.html', context)


def create_checkout_session(request, id):
    item = get_object_or_404(Item, pk=id)
    line_items = build_line_items([item])
    session = stripe.checkout.Session.create(
        line_items=line_items,
        mode='payment',
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )
    return JsonResponse({'id': session.id})


def create_checkout_session_order(request, id):
    order = get_object_or_404(Order, pk=id)
    items = order.items.all()
    line_items = build_line_items(items)
    discounts = []
    if order.discount:
        coupon = stripe.Coupon.create(
            percent_off=order.discount.percentage,
            duration='once',
        )
        discounts.append({"coupon": coupon.id})

    if order.tax:
        tax_rate = stripe.TaxRate.create(
            display_name=order.tax.name,
            percentage=order.tax.percentage,
            inclusive=False,
        )

    line_items = build_line_items(items, tax_rate)
    session = stripe.checkout.Session.create(
        line_items=line_items,
        mode='payment',
        discounts=discounts if discounts else None,
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )
    return JsonResponse({'id': session.id})


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')
