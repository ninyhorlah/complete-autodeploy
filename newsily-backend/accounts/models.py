from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email'), unique=True)
    username = models.CharField(_('username'), unique=True, max_length=255)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['username']

    def __str__(self):
        return self.email
