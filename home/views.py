# home/views.py

from django.shortcuts import render
from yachts.models import Yacht
import random

def home(request):
    yachts = list(Yacht.objects.all())
    random_yachts = random.sample(yachts, 3) if len(yachts) >= 3 else yachts
    deal_yacht = random.choice(yachts) if yachts else None 

    context = {
        'yachts': random_yachts,
        'deal_yacht': deal_yacht,
    }
    return render(request, 'home/index.html', context)