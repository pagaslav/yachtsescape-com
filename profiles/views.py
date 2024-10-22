""" profiles/views.py """

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm, YachtForm
from booking.models import Booking
from django.conf import settings
from yachts.models import Yacht
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import user_passes_test, login_required
from cloudinary.uploader import destroy


def is_admin(user):
    """ Check if the user is an admin or staff member """
    return user.is_superuser or user.is_staff


def profile(request):
    """ Display the user's profile with confirmed bookings """
    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)
        confirmed_bookings = Booking.objects.filter(
            user=request.user, status='confirmed'
        )
        context = {
            'user': request.user,
            'profile': user_profile,
            'confirmed_bookings': confirmed_bookings,
        }
        return render(request, 'profiles/profile.html', context)
    else:
        messages.error(request, 'You must be logged in to view your profile.')
        return redirect('account_login')


@login_required
def profile_edit(request):
    """ Allow the user to edit their profile and send confirmation email """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            subject = (
                f'Profile Update Confirmation for {request.user.username}'
            )
            message = (
                f'Hello {request.user.username},\n\n'
                'Your profile has been updated successfully.\n\n'
                'Here are the updated details:\n'
                f'First Name: {user_profile.first_name}\n'
                f'Last Name: {user_profile.last_name}\n'
                f'Email: {request.user.email}\n'
                f'Phone: {user_profile.phone_number}\n'
                f'Address: {user_profile.street_address1}, '
                f'{user_profile.street_address2}, '
                f'{user_profile.town_city}, {user_profile.county_state}, '
                f'{user_profile.postal_code}, {user_profile.country}\n\n'
                'If you did not make these changes, please contact support '
                'immediately.'
            )
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [request.user.email],
                fail_silently=False,
            )

            messages.success(
                request,
                f'Profile updated successfully, and a confirmation email '
                f'has been sent to {request.user.email}!'
            )
            return redirect('profile')
        else:
            messages.error(
                request,
                'There was an error updating your profile. Please check '
                'the form and try again.'
            )
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profiles/profile_edit.html', {'form': form})


@user_passes_test(is_admin)
def yachts_management(request):
    """ Display all yachts in the management page """
    yachts = Yacht.objects.all()
    if not yachts:
        messages.info(request, 'No yachts available.')
    return render(
        request,
        'profiles/yachts_management.html',
        {'yachts': yachts}
    )


@user_passes_test(is_admin)
def add_yacht(request):
    """ Add a new yacht to the management system """
    form = YachtForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Yacht created successfully!')
            return redirect('yachts_management')
        else:
            messages.error(
                request,
                'The Yacht could not be created because the data didn\'t '
                'validate.'
            )

    return render(request, 'profiles/add_yacht.html', {'form': form})


@user_passes_test(is_admin)
def edit_yacht(request, yacht_id):
    """ Edit an existing yacht's details """
    yacht = get_object_or_404(Yacht, id=yacht_id)

    if request.method == 'POST':
        form = YachtForm(request.POST, request.FILES, instance=yacht)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'Yacht "{yacht.name}" was updated successfully!'
            )
            return redirect('yachts_management')
        else:
            messages.error(
                request,
                'There was an error updating the yacht. Please check the '
                'form and try again.'
            )
    else:
        form = YachtForm(instance=yacht)

    return render(
        request, 'profiles/edit_yacht.html', {'form': form, 'yacht': yacht}
    )


@user_passes_test(is_admin)
def delete_yacht(request, yacht_id):
    """ Delete an existing yacht """
    yacht = get_object_or_404(Yacht, id=yacht_id)

    if request.method == 'POST':
        try:
            if yacht.card_image:
                public_id = yacht.card_image.public_id
                if public_id:
                    destroy(public_id)

            yacht.delete()
            messages.success(
                request, f'Yacht "{yacht.name}" deleted successfully!'
            )
        except Exception as e:
            messages.error(request, f'Error deleting yacht: {str(e)}')

        return redirect('yachts_management')

    return redirect('yachts_management')


@user_passes_test(is_admin)
def users_management(request):
    """ Display all users in the management page """
    users = User.objects.all()
    if not users:
        messages.info(request, 'No users found.')
    return render(request, 'profiles/users_management.html', {'users': users})


@user_passes_test(is_admin)
def edit_user(request, user_id):
    """ Edit an existing user's details and profile """
    user = get_object_or_404(User, pk=user_id)
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        username = request.POST.get('username')

        if not username:
            messages.error(
                request, f'Username for {user.username} cannot be empty.'
            )
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
            messages.success(
                request,
                f'Password for {user.username} changed successfully.'
            )
        elif new_password and new_password != confirm_password:
            messages.error(
                request,
                f'New passwords for {user.username} do not match.'
            )

        messages.success(
            request, f'Profile for {user.username} updated successfully.'
        )
        return redirect('users_management')

    return render(
        request,
        'profiles/edit_user.html',
        {'user': user, 'profile': profile}
    )


@user_passes_test(is_admin)
def delete_user(request, user_id):
    """ Delete an existing user """
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        username = user.username
        user.delete()
        messages.success(request, f'User "{username}" deleted successfully!')
        return redirect('users_management')

    return redirect('users_management')
