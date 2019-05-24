from django.db import models
# from django.contrib.auth.models import User,AbstractUser
from django.contrib.auth.models import UserManager,AbstractUser,AbstractBaseUser,PermissionsMixin
from django.contrib.auth import get_user_model
from django.contrib import auth

# Create your models here.
# class Person(User):
#     class Meta:
#         proxy = True
#
#     @classmethod
#     def get_blacklist(cls):
#         return cls.objects.filter(is_active=False).all()
#
#
#
# class UserExtension(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='extension')
#     phone = models.CharField(max_length=100)
#     school = models.CharField(max_length=100,null=True,blank=True)
#
#
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# @receiver(post_save,sender=User)
# def handle_user_extension(sender,instance,created,**kwargs):
#     if created:
#         UserExtension.objects.create(user=instance)
#         print('create_success')
#     else:
#         instance.extension.save()
#         print('extension save')

class User_Manager(UserManager):
    def _create_user(self, phone,username, password, **extra_fields):
        if not phone:
            raise ValueError("必须要传递手机号码")
        if not password:
            raise ValueError("必须要传递密码")
        user = self.model(username=username,phone=phone,**extra_fields)
        user.set_password(password)
        user.save()


    def create_user(self,phone,username,password, **extra_fields):
        extra_fields['is_superuser'] = False
        return self._create_user(phone,username,password,**extra_fields)

    def create_superuser(self,phone,username,password, **extra_fields):
        extra_fields['is_superuser'] = True
        return self._create_user(phone,username,password,**extra_fields)



# class User(AbstractUser):
#     phone = models.CharField(max_length=100,unique=True)
#     school = models.CharField(max_length=100)
#
#     USERNAME_FIELD = 'phone'
#
#     objects = User_Manager()

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=20)
    phone = models.CharField(max_length=100,unique=True)
    school = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'phone'
    objects = User_Manager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        """Return the short name for the user."""
        return self.username


class ArticleModel(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
