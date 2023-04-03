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
        # 防止migrate的时候生成一张表
        abstract = True


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="Nickname/昵称", default="")
    birthday = models.DateField(verbose_name="Birthday/生日", null=True, blank=True)
    gender = models.CharField(verbose_name="Gender/性别", choices=GENDER_CHOICES, max_length=6)
    address = models.CharField(max_length=100, verbose_name="Address/地址", default="")
    mobile = models.CharField(max_length=11, verbose_name="Phone Number/电话")
    image = models.ImageField(verbose_name="Avatar/头像", upload_to="head_image/%Y/%m", default="default.jpg")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username
