from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.apps import apps
from django.contrib.auth.hashers import make_password

# Create your models here.
class CustomUserMnager(UserManager):
    def _create_user(self,first_name,last_name,birthday,address,gender, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(first_name=first_name,last_name=last_name,birthday=birthday,address=address,gender=gender,username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    

    def create_superuser(self,first_name,last_name,birthday,address,gender, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(first_name,last_name,birthday,address,gender,username, email, password, **extra_fields)

class Members(AbstractUser):
    objects =CustomUserMnager()
    REQUIRED_FIELDS = ["first_name","last_name","birthday","email","mobile_number","gender","address"]
    mobile_number = models.CharField(max_length=11)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    birthday=models.DateField()
    address=models.CharField(max_length=100)

