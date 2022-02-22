from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class WebUser(User):
    mobile = models.TextField(max_length=11, unique=True)

    class Meta:
        verbose_name = "客户"
        verbose_name_plural = "客户"
