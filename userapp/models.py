from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    """Custom user model extending AbstractUser."""
    pass
