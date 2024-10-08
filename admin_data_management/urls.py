
from django.urls import path
from . views import UserRegistration, Admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
     path('registration', UserRegistration.as_view({'post': 'create', 'get': 'list'})),
     path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('admin', Admin.as_view({'get':'list'})),
     path('admin/<int:id>', Admin.as_view({ 'patch': 'partial_update'})),
]