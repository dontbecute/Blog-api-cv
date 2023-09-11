from django.db import models

from django.conf import settings
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    post = models.TextField(max_length=1024)
    auth = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE )
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title