""" home/views.py """

from django.shortcuts import render
from yachts.models import Yacht
from django.http import HttpRequest
from django.core.exceptions import PermissionDenied
from django.core.exceptions import SuspiciousOperation
import random


def home(request):
    """ Render the homepage with random yachts and a deal of the week yacht """
    yachts = list(Yacht.objects.all())
    random_yachts = random.sample(yachts, 3) if len(yachts) >= 3 else yachts
    deal_yacht = random.choice(yachts) if yachts else None
    default_image_url = 'url_to_default_image'

    for yacht in random_yachts:
        yacht.card_image_url = (
            yacht.card_image.url if yacht.card_image else default_image_url
        )

    context = {
        'yachts': random_yachts,
        'deal_yacht': deal_yacht,
        'default_image_url': default_image_url,
    }
    return render(request, 'home/index.html', context)
