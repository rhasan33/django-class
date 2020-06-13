from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


class User(AbstractBaseUser):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    )

    STATUS = (
        ('active', 'Active'),
        ('archived', 'Archived'),
        ('deleted', 'Deleted'),
    )

    first_name = models.CharField(max_length=255, )
    last_name = models.CharField(max_length=255, )
    is_active = models.BooleanField(default=True, )
    is_staff = models.BooleanField(default=False, )
    is_superuser = models.BooleanField(default=False, )
    gender = models.CharField(max_length=20, choices=GENDER, default='male')
    email = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    status = models.CharField(max_length=20, choices=STATUS, default='active')
    username = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender', 'is_superuser', 'is_staff', 'is_active', 'status']
    objects = UserManager()
    last_login = None

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

