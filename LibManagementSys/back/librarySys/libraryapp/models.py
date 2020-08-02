from django.db import models
from django.contrib.auth.models import AbstractUser


 #userProfile继承AbstractUser分类，进行拓展
class UserProfile(AbstractUser):
    """
    用户类拓展
    """
    avatar = models.CharField(max_length=100, null=True, blank=True, verbose_name="avatar")
    usertype = models.CharField(max_length=10, default="editor", verbose_name="role")
    introduction = models.TextField(max_length=500,null=True,blank=True, verbose_name="introduction")

    class Meta:
        verbose_name = "user"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username