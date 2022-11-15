from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

def createSuperUser(request):
    admin = os.system("python manage.py createsuperuser")
    return admin

def createUser(request):
    user = os.system("python manage.py createsuperuser")
    return user

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def get_profile_image_filepath(self, filename):
    return 'profile_images/' + str(self.pk) + '/profile_image.png'

def get_default_profile_image():
    return 'default_profile.png'

class Users(AbstractBaseUser):

    email               =models.EmailField(max_length=60,verbose_name="email", unique=True)
    username            =models.CharField(max_length=30,verbose_name="username", unique=True)
    date_joined         =models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_lo             =models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin            =models.BooleanField(default=False)
    is_staff            =models.BooleanField(default=False)
    is_active           =models.BooleanField(default=True)
    is_superuser        =models.BooleanField(default=False)
    profile_pic         =models.ImageField(max_length=255,upload_to= get_profile_image_filepath , default=get_default_profile_image ,null=True,blank=True)
    hide_email          =models.BooleanField(default=True)


    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index('profile_images/' + str(self.pk) + "/"):]
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True