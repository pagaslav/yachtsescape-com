# checkout/admin.py

from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    # Fields to display in readonly mode
    readonly_fields = ('order_number', 'date', 'total_cost', 'stripe_pid')
    
    # Fields to display in the order form within the admin panel
    fields = ('order_number', 'user_profile', 'booking', 'date', 
              'full_name', 'email', 'phone_number', 'country', 
              'postcode', 'town_or_city', 'street_address1', 
              'street_address2', 'county', 'total_cost', 'stripe_pid', 
              'status')
    
    # Fields to display in the list of orders
    list_display = ('order_number', 'date', 'full_name', 'total_cost', 'status')
    
    # Ordering of the list display
    ordering = ('-date',)

# Registering the Order model with the custom admin options
admin.site.register(Order, OrderAdmin)