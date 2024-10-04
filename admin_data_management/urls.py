
from django.urls import path
from . views import UserRegistration
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
     path('registration', UserRegistration.as_view({'post': 'create', 'get': 'list'})),
     path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]