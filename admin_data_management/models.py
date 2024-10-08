from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager



class UserManager(BaseUserManager):
     def create_user(self, email, password=None, **extra_fields):
          if not email:
               raise ValueError("Please provide an email address")
          
          email = self.normalize_email(email)
          user = self.model(email = email, **extra_fields)
          user.set_password(password)
          user.save()
          return user
     
     def create_superuser(self, email, password=None, **extra_fields):
          extra_fields.setdefault('is_staff', True)
          extra_fields.setdefault('is_superuser', True)
          extra_fields.setdefault('user_type', 1)
          
          if extra_fields.get('is_staff') is not True:
               raise ValueError("Superuser must have is_Staff set to True")
          
          if extra_fields.get('is_superuser') is not True:
               raise ValueError("Superuser must have is_SuperUser set to True")
          
          user = self.create_user(email=email, password=password, **extra_fields)
          return user
     
     
class User(AbstractUser):
     USER_TYPES = (
          (1, 'Admin'),
          (2, 'Staff'),
     )
     
     user_type = models.PositiveSmallIntegerField(choices=USER_TYPES, default=2)
     email = models.EmailField(unique=True, max_length=80)
     username = models.CharField(max_length=80)
     first_name = models.CharField(max_length=80)
     last_name = models.CharField(max_length=80)
     last_login = models.DateTimeField(auto_now_add=True)
     is_staff = models.BooleanField(default=True)
     is_active = models.BooleanField(default=True)
     is_superuser = models.BooleanField(default=False)
     
     objects = UserManager()
     USERNAME_FIELD = 'email'
     REQUIRED_FIELDS =['first_name', 'last_name' ,'username']
     
     def has_perm(self, perm, obj=None):
          return self.is_superuser
     
     def has_module_perms(self, app_label):
          return True
     
     def __str__(self):
          return self.username