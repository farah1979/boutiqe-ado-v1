from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVARY_THRESHOLD:
        delivary = total * Decimal(settings.STANDARD_DELIVARY_PRECENTAGE/100)
        free_delivary_delta = settings.FREE_DELIVARY_THRESHOLD - total
    else:
        delivary = 0
        free_delivary_delta = 0

    grand_total = delivary + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivary': delivary,
        'free_delivary_delta': free_delivary_delta,
        'grand_total': grand_total,
        'free_delivary_threshold': settings.FREE_DELIVARY_THRESHOLD
    }

    return context
