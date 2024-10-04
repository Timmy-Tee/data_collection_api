from rest_framework import viewsets, mixins
from . models import CustomerDetail
from . serializers import CustomerSerializer
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class DataCollectionView(mixins.CreateModelMixin, mixins.ListModelMixin ,viewsets.GenericViewSet):  
     authentication_classes = [JWTAuthentication]
     permission_classes = [IsAuthenticated]
     
     queryset = CustomerDetail.objects.all()
     serializer_class = CustomerSerializer
     
     def create(self, request, *args, **kwargs):
          serializer = self.get_serializer(data = request.data)
          
          if serializer.is_valid(raise_exception=True):
               serializer.save()
               return Response({'message': "Customer Created Successfully", 'data': serializer.data}, status=status.HTTP_201_CREATED)

