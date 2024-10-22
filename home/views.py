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


def handler404(request, exception):
    """ Handle 404 errors and render the custom 404 error page """
    return render(request, 'errors/404.html', status=404)


def handler500(request):
    """ Handle 500 errors and render the custom 500 error page """
    return render(request, 'errors/500.html', status=500)


def handler403(request, exception):
    """ Handle 403 errors and render the custom 403 error page """
    return render(request, 'errors/403.html', status=403)


def handler400(request, exception):
    """ Handle 400 errors and render the custom 400 error page """
    return render(request, 'errors/400.html', status=400)


def test_500_error(request: HttpRequest):
    """ Raise a test exception for the 500 error handler """
    raise Exception("Test 500 error")


def test_403_error(request):
    """ Raise a test exception for the 403 error handler """
    raise PermissionDenied("Test 403 error")


def test_400_error(request):
    """ Raise a test exception for the 400 error handler """
    raise SuspiciousOperation("Test 400 error")
