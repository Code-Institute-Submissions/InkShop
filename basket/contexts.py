"""
Shopping basket context processor
"""
from django.conf import settings
from django.shortcuts import get_object_or_404
from decimal import Decimal

from products.models import Supplies


def basket_contents(request):
    basket_items = []
    sub_total = 0
    total_vat = 0
    basket_total = 0

    basket = request.session.get('basket', {})

    for item, quantity in basket.items():
        product = get_object_or_404(Supplies, pk=item)
        sub_total += quantity * product.price
        total_vat += (product.calculate_inc_vat_price() -
                      product.price) * quantity
        basket_items.append({
            'id': item,
            'quantity': quantity,
            'product': product,
        })

    if sub_total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.DELIVERY_CHARGE
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - sub_total
    else:
        delivery = 0
        free_delivery_delta = 0

    # not including delivery charge unless items have been added to basket
    if sub_total > 0:
        basket_total = sub_total + total_vat + delivery
    else:
        basket_total = 0

    context = {
        'basket_items': basket_items,
        'sub_total': sub_total,
        'delivery': delivery,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'free_delivery_delta': free_delivery_delta,
        'total_vat': total_vat,
        'basket_total': basket_total,
    }

    return context