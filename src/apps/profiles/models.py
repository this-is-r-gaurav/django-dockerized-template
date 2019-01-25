
from django.db import models
from django.contrib.auth.models import User
from .utils import default_avatar_image_path




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isInstructor = models.BooleanField(default=False)
    updatedAt = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to=default_avatar_image_path, default=default_avatar_image_path)

    def __str__(self):
        return self.user.username





