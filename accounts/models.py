from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    user_photo = models.ImageField(upload_to='profile/%Y/%m/%d/')
    user_phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username