from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('admin_data_management.urls')),
    path('user/', include('user_data_collection.urls')),

]
