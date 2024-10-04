from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate


class UserRegistrationSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = ['username','first_name', 'last_name', 'email', 'password']
          extra_kwargs = {
               'password': {'write_only': True}
          }
          
     def create(self, validated_data):
          try:
               user = User.objects.create(**validated_data)
               user.set_password(validated_data['password'])
               user.save()
               return user
          except Exception as e:
               return f'{str(e)}'
     
     
class UserLoginSerializer(serializers.ModelSerializer):
     
     email = serializers.CharField()
     password = serializers.CharField(write_only=True)
    
     class Meta:
          model = User
          fields = ['email', 'password']
          
     def validate(self, validated_data):
          user = authenticate(**validated_data)
          if user and user.is_staff:
               validated_data['user'] = user
               return validated_data
          else:
               raise serializers.ValidationError({'message': "Incorrect email or Password"})
          
          
