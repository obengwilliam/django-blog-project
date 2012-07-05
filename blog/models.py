from django.db import models
from django.contrib import admin


# Create your models here.
class Post(models.Model):
       title=models.CharField(max_length=60)
       body=models.TextField()
       created=models.DateField(auto_now=True)
       updated=models.DateField(auto_now=True)
       def __unicode__(self):
             return self.title,self.created,self.updated


class Comment(models.Model):
       body=models.TextField()
       author=models.TextField(max_length=60)
       created=models.DateField(auto_now=True)
       updated=models.DateField(auto_now=True)
       post=models.ForeignKey(Post,related_name='post')
       def __unicode__(self):
             return self.author,self.created,self.updated




admin.site.register(Post)
admin.site.register(Comment)

