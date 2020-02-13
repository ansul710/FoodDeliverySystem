from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.
class UserProfilesManager(BaseUserManager):
    def create_user(self, email, name, password, phone):
        if not email:
            raise ValueError('Enter Email address')
        if not password:
            raise ValueError('Enter your password')
        if not phone:
            raise ValueError('User must enter their Phone number')

        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password, phone):
        user = self.create_user(email, name, password, phone)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfiles(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=10, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfilesManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']
