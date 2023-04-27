from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.


class  Article(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
 
    def __str__(self):
        return f"{self.title} - {self.content[:50]}"
    
class BlogComment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')
    timestamp = models.DateTimeField(default=now)
    
    



    