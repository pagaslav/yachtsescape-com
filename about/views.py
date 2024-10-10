from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = 'about/about.html'

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('about')
    else:
        form = ReviewForm()
    return render(request, 'about/add_review.html', {'form': form})