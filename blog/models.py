from django.db import models
from django.contrib import admin




# Create your models here.
class Post(models.Model):
       title=models.CharField(max_length=60)
       body=models.TextField()
       Datecreated=models.DateField(auto_now=True)
       Dateupdated=models.DateField(auto_now=True)
       def Firstsixtycharacters(self):
           return self.body[:60]
       def __unicode__(self):
             return self.title


class Comment(models.Model):
       author=models.CharField(max_length=60)
       body=models.TextField()
       Datecreated=models.DateField(auto_now=True)
       Dateupdated=models.DateField(auto_now=True)
       post=models.ForeignKey(Post,related_name='comments')
       def Firstsixtycharacters(self):
           return self.body[:60]
       def __unicode__(self):
             return self.author

#admin.site.register(Post)
#admin.site.register(Comment)
class CommentInline(admin.TabularInline):     
      model=Comment

#class BlogAdmin(admin.ModelAdmin):
#     inlines=[Comment,]

class PostAdmin(admin.ModelAdmin):
      list_display=('title','Datecreated','Dateupdated')
      search_fields=('title','body')
      list_filter=('Datecreated',)
      inlines=[CommentInline]

      
     

class CommentAdmin(admin.ModelAdmin):
      list_display=('post','author','body','Firstsixtycharacters','Datecreated','Dateupdated')
      list_filter=('Datecreated','Dateupdated')






admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
#admin.site.register(BlogAdmin)










      
       
