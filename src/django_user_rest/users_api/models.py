from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfilesManager(BaseUserManager):
    """ Helps Django to work with our custom user model."""

    def create_user(self, email, name, password=None):
        """ Creates a new user profile object. """

        if not email:
            raise ValueError("Users must have email address!")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        
        user.set_password(password)     # it is used to hash the passwprd of the user
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """ Creates a new super user profile object. """

        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user



        

class UserProfiles(AbstractBaseUser, PermissionsMixin):
    """ Represents the user profiles in the application. Extension of Django base model."""

    user_email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default=True)   # mandatory field when overwriting default user model of django
    is_staff = models.BooleanField(default=False)   # mandatory field when overwriting default user model of django

    objects = UserProfilesManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name'] # as email is already reqired due to being USERNAME_FIELD

    def get_full_name(self):
        """ Used to get full name of user """

        return self.name 

    def get_short_name(self):
        """ Used to get short name of user """

        return self.name 

    def __str__(self):
        """ Django uses this when it needs to convert a object to string  """

        return self.email