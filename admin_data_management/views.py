from rest_framework import mixins, viewsets
from rest_framework.views import APIView
from .serializer import UserRegistrationSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework import status
from . models import User
from user_data_collection . models import CustomerDetail
from rest_framework.parsers import JSONParser
from django.contrib.auth import logout, login
from rest_framework.permissions import AllowAny, IsAdminUser
from .serializer import CustomerDetailSerializer
from rest_framework.decorators import action



# Create your views here.
class UserRegistration(mixins.CreateModelMixin, mixins.ListModelMixin , viewsets.GenericViewSet):
     permission_classes = [AllowAny]
     queryset = User.objects.all()
     serializer_class = UserRegistrationSerializer
     
     def create(self, request, *args, **kwargs):
          serializer_class = self.get_serializer(data=request.data)
          if serializer_class.is_valid(raise_exception=True):
               serializer_class.save()
               return Response({'message': "User Registration Was Successful"}, status=status.HTTP_201_CREATED)
          
          
class UserLogin(APIView):
     permission_classes = [AllowAny]
     parser_classes = [JSONParser]
     
     def post(self, request):
          serializer = UserLoginSerializer(data = request.data)
          if serializer.is_valid(raise_exception=True):
               user = serializer.validated_data['user']
               login(request, user)
               print(serializer.data, serializer.validated_data)
               return Response({'message': "Login Successful", 'data': serializer.data}, status=status.HTTP_200_OK)
          

class Admin(viewsets.ModelViewSet):
     permission_classes = [IsAdminUser]
     
     queryset = CustomerDetail.objects.all()
     serializer_class = CustomerDetailSerializer
     lookup_field = 'id'

     def update_customer_status(self, request):
        updated = User.objects.filter(id__in=request.data['id']).update(status='Done')
        return Response({'message': f'{updated} customers\' status updated to \'Done\''}, status=status.HTTP_200_OK)