from django.shortcuts import render, get_object_or_404
from .models import Yacht

# View to display a list of yachts
def yacht_list(request):
    yachts = Yacht.objects.all()  # Get all yacht objects
    return render(request, 'yachts/yacht-list.html', {'yachts': yachts})

# View to display details of a specific yacht
def yacht_detail(request, yacht_id):
    yacht = get_object_or_404(Yacht, id=yacht_id)  # Get yacht by ID or return 404
    return render(request, 'yachts/yacht-detail.html', {'yacht': yacht})