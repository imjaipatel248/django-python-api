from django.db import models
import sys
sys.path.append("..")
from users.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    tags = models.TextField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title