import secrets

from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, username=None, image=None, **extra_fields):
        if not email:
            raise ValueError('The email is required to create this user')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, image=image, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        user.verification_token = secrets.token_urlsafe(32)
        user.save()

        return user

    def create_superuser(self, email, password=None, username=None, image=None, **extra_fields):
        user = self.create_user(email, password, username=username, image=image, **extra_fields)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user