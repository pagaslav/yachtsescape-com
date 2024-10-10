from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

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