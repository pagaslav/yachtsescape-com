# profiles/urls.py

from django.urls import path
from .views import profile, profile_edit, yachts_management, add_yacht, edit_yacht, delete_yacht, users_management, edit_user, delete_user

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('yachts/management/', yachts_management, name='yachts_management'),
    path('add/', add_yacht, name='add_yacht'), 
    path('edit/<int:yacht_id>/', edit_yacht, name='edit_yacht'), 
    path('delete/<int:yacht_id>/', delete_yacht, name='delete_yacht'), 
    path('users/management/', users_management, name='users_management'), 
    path('users/edit/<int:user_id>/', edit_user, name='edit_user'), 
    path('users/delete/<int:user_id>/', delete_user, name='delete_user'),
]