from django.db import models
from django.contrib.auth.models import (AbstractUser)
# Create your models here.

class MyUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
    
    @property
    def displayName(self):
        return self.first_name + ' ' + self.last_name

 
