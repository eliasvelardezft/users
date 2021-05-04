from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    gender_choices = [
        ['M', 'Masculino'],
        ['F', 'Femenino'],
        ['O', 'Otro']
    ]

    username = models.CharField("Username", max_length=10, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=40, blank=True)
    apellidos = models.CharField(max_length=40, blank=True)
    genero = models.CharField("Genero", max_length=1, choices=gender_choices, blank=True)
    #
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = [
        'email',
    ]

    objects = UserManager()

    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return f'{self.nombres} {self.apellidos}'
    
    def __str__(self):
        return f'{self.id}-{self.username}'

    
    
