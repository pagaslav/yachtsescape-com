from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm, YachtForm
from booking.models import Booking 
from yachts.models import Yacht
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_superuser or user.is_staff

def profile(request):
    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)
        confirmed_bookings = Booking.objects.filter(user=request.user, status='confirmed')
        context = {
            'user': request.user,
            'profile': user_profile,
            'confirmed_bookings': confirmed_bookings, 
        }
        return render(request, 'profiles/profile.html', context)
    else:
        return render(request, 'profiles/login_required.html')  

def profile_edit(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profiles/profile_edit.html', {'form': form})

@user_passes_test(is_admin)
def yachts_management(request):
    yachts = Yacht.objects.all()  
    return render(request, 'profiles/yachts_management.html', {'yachts': yachts})

@user_passes_test(is_admin)
def add_yacht(request):
    form = YachtForm(request.POST or None, request.FILES or None) 

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Yacht created successfully!')
            return redirect('yachts_management')
        else:
            print(form.errors)
            messages.error(request, 'The Yacht could not be created because the data didn\'t validate.')

    return render(request, 'profiles/add_yacht.html', {'form': form})

@user_passes_test(is_admin)
def edit_yacht(request, yacht_id):
    yacht = get_object_or_404(Yacht, id=yacht_id)
    
    if request.method == 'POST':
        form = YachtForm(request.POST, request.FILES, instance=yacht)
        if form.is_valid():
            form.save()
            messages.success(request, 'Yacht updated successfully!')
            return redirect('yachts_management') 
    else:
        form = YachtForm(instance=yacht)

    return render(request, 'profiles/edit_yacht.html', {'form': form, 'yacht': yacht})

@user_passes_test(is_admin)
def delete_yacht(request, yacht_id):
    yacht = get_object_or_404(Yacht, id=yacht_id)

    if request.method == 'POST':
        try:
            # Удаление карточного изображения, если оно существует
            if yacht.card_image: 
                image_name = yacht.card_image.name
                if image_name: 
                    default_storage.delete(image_name) 
            # Удаление яхты
            yacht.delete() 
            messages.success(request, 'Yacht deleted successfully!')
        except Exception as e:
            messages.error(request, f'Error deleting yacht: {str(e)}')
        return redirect('yachts_management') 

    return redirect('yachts_management')

@user_passes_test(is_admin)
def users_management(request):
    users = User.objects.all() 
    return render(request, 'profiles/users_management.html', {'users': users})

@user_passes_test(is_admin)
def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        username = request.POST.get('username')
        
        if not username:
            messages.error(request, 'Username cannot be empty.')
            return redirect('edit_user', user_id=user.id)

        user.username = username
        user.email = request.POST.get('email')
        user.save()

        profile.first_name = request.POST.get('first_name')
        profile.last_name = request.POST.get('last_name')
        profile.phone_number = request.POST.get('phone_number')
        profile.street_address1 = request.POST.get('street_address1')
        profile.street_address2 = request.POST.get('street_address2')
        profile.town_city = request.POST.get('town_city')
        profile.county_state = request.POST.get('county_state')
        profile.postal_code = request.POST.get('postal_code')
        profile.country = request.POST.get('country')
        profile.save()

        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password and new_password == confirm_password:
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully.')
        elif new_password and new_password != confirm_password:
            messages.error(request, 'New passwords do not match.')

        messages.success(request, 'Profile updated successfully.')
        return redirect('users_management')

    return render(request, 'profiles/edit_user.html', {'user': user, 'profile': profile})

@user_passes_test(is_admin)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully!')
        return redirect('users_management')

    return render(request, 'profiles/delete_user_confirmation.html', {'user': user})