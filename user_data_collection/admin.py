from django.contrib import admin
from . models import CustomerDetail
from django.contrib import messages

# Register your models here.

class DataCollectionAdmin(admin.ModelAdmin):
     list_display = ['customer_name', 'status']
     ordering = ['customer_name']
     actions = ['update_customer_status']
     
     @admin.action(description="Update Customer Status Choice")
     def update_customer_status(self, request, queryset):
         updated = queryset.update(status='Done')
         self.message_user(
              request, 
              f"{updated} customers' status updated to 'Done'."
         )
         messages.SUCCESS
          
admin.site.register(CustomerDetail, DataCollectionAdmin)