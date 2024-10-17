# profiles/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from booking.models import Booking  # Import the Booking model

def profile(request):
    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)
        confirmed_bookings = Booking.objects.filter(user=request.user, status='confirmed')
        context = {
            'user': request.user,
            'profile': user_profile,
            'confirmed_bookings': confirmed_bookings,  # Add bookings to context
        }
        return render(request, 'profiles/profile.html', context)
    else:
        return render(request, 'profiles/login_required.html')  # Optional: Inform the user to log in

def profile_edit(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profiles/profile_edit.html', {'form': form})