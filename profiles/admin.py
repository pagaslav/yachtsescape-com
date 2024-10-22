""" profiles/admin.py """

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """ Admin interface for managing user profiles """

    list_display = (
        'user', 'first_name', 'last_name', 'phone_number', 'street_address1',
        'street_address2', 'town_city', 'county_state',
        'postal_code', 'country'
    )

    search_fields = (
        'user__username', 'phone_number', 'street_address1', 'town_city'
    )

    list_filter = ('country', 'county_state')


class UserProfileInline(admin.StackedInline):
    """ Inline admin interface for linking profiles with users """

    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class UserAdmin(BaseUserAdmin):
    """ Admin interface for managing users, with profile inline support """

    inlines = (UserProfileInline,)

    def get_inline_instances(self, request, obj=None):
        """ Ensure inline instances are returned only for existing users """
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)


# Unregister the default User admin and register the custom one
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
