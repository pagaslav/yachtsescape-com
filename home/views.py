# home/views.py
from django.shortcuts import render
from .models import Yacht  # Import the Yacht model for searching

# View for the home page
def index(request):
    return render(request, 'home/index.html')

# View for handling search results
def search_results(request):
    query = request.GET.get('q')  # Get the search query from the request
    results = []
    if query:
        # Perform search across the Yacht model based on the name
        results = Yacht.objects.filter(name__icontains=query)
    # Render the search results page with the query and results
    return render(request, 'home/search-results.html', {'results': results, 'query': query})