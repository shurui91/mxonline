from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (
    ("male", "Male"),
    ("female", "Female")
)


class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        abstract = True


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="Nickname", default="")
    birthday = models.DateField(verbose_name="Birthday", null=True, blank=True)
    gender = models.CharField(verbose_name="Gender", choices=GENDER_CHOICES, max_length=6)
    address = models.CharField(max_length=100, verbose_name="Address", default="")
    mobile = models.CharField(max_length=11, verbose_name="Phone Number")
    image = models.ImageField(verbose_name="Avatar", upload_to="head_image/%Y/%m", default="default.jpg")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
