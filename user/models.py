from django.conf.global_settings import MEDIA_URL,STATIC_URL
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


# Create your models here.
from django.forms import model_to_dict


class User(AbstractUser):
    imagen = models.ImageField(upload_to='images/user/', null=True, blank=True)

    def get_image(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def toJSON(self):
         item = model_to_dict(self,exclude=['password'])
         item['last_login'] = self.last_login.strftime('%Y-%m-%d')
         item['date_joined'] = self.last_login.strftime('%Y-%m-%d')
         item['imagen'] = self.get_image()
         return item