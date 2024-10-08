# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import login
# from .forms import UserRegistrationForm, ProfileForm

# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         profile_form = ProfileForm(request.POST)

#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save(commit=False)
#             user.set_password(user_form.cleaned_data['password']) 
#             user.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user 
#             profile.save()

#             login(request, user) 
#             messages.success(request, 'Registration successful!')
#             return redirect('profile') 
#     else:
#         user_form = UserRegistrationForm()
#         profile_form = ProfileForm()

#     return render(request, 'profiles/register.html', {
#         'user_form': user_form,
#         'profile_form': profile_form,
#     })

# def profile(request):
#     return render(request, 'profiles/profile.html')  