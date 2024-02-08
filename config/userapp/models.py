from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

from userapp.managers import CustomUserManager


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField("Email", unique=True)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    username = models.CharField("User Name", max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=f'avatars/{email}', blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}-{self.pk}"

    class Meta:
        permissions = [
            ("can_change_user_permissions", "Can change user permissions"),
        ]
        default_permissions = ()