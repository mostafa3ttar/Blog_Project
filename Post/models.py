from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

# user - title - img - content - created

class Post (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    content = models.TextField(default=' ')
    img = models.ImageField(upload_to='post_img/%y%m%d', null=True, blank=True)
    # img = models.ImageField(upload_to='post_img/%y%m%d', default='post_img/default.png')
    created = models.DateTimeField(default=timezone.now)
    
    active = models.BooleanField(default=True)
    
    #to appeare the name of the data we added in admin panel
    def __str__(self):
        return self.title