from django.urls import path
from .views import DataCollectionView

urlpatterns = [
     path('add_data', DataCollectionView.as_view({'post': 'create', 'get': 'list'}),)
]