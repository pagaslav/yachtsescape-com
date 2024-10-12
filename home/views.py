# home/views.py

from django.shortcuts import render
from yachts.models import Yacht
import random

# View for handling search results
def search_results(request):
    query = request.GET.get('q')  # Get the search query from the request
    results = []
    if query:
        # Perform search across the Yacht model based on the name
        results = Yacht.objects.filter(name__icontains=query)
    # Render the search results page with the query and results
    return render(request, 'home/search-results.html', {'results': results, 'query': query})


# View for the home page, displaying random yachts
def home(request):
    yachts = list(Yacht.objects.all())
    random_yachts = random.sample(yachts, 3) if len(yachts) >= 3 else yachts
    deal_yacht = random.choice(yachts) if yachts else None  # Select a single random yacht

    context = {
        'yachts': random_yachts,
        'deal_yacht': deal_yacht,
    }
    return render(request, 'home/index.html', context)