# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.shortcuts import render_to_response
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from models import Post, Comment 

@login_required
def post_list(request):
    posts = Post.objects.all()
    c=Context({'posts':posts,'user':request.user})
    return render_to_response('blog/post_list.html',c)



class CommentForm(ModelForm):
	class Meta:
              model=Comment
              exclude=['post','author']#exclude=('post'),or fields=('')



@csrf_exempt
def edit_comment(request,id): 
    edit=Comment.objects.get(pk=id)
    if request.method =='POST':
        form=CommentForm(request.POST,instance=edit)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(edit.post.get_absolute_url())
    else:
        form=CommentForm(instance=edit)
    if str(request.user)== str(edit):
        return render_to_response('blog/edit_comment.html',{'comment':edit,'form':form,'user':request.user})
    else:
        return HttpResponseForbidden('This is forbidden')

       
@csrf_exempt
@login_required
def post_detail(request, id, showComments=False):
   posts=Post.objects.get(pk=id)
 
   comments=posts.comments.all()
   if request.method =='POST':
        comment=Comment(post=posts)
        comment.author=request.user
        form=CommentForm(request.POST,instance=comment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
   else:
        form=CommentForm()
        
   return render_to_response('blog/post_detail.html',{'posts':posts,'comments':comments,'form':form,'user':request.user})

def post_search(request, term):
    if request.GET.get('q','')!='':
	 term=request.GET.get('q','')
    posts=Post.objects.filter(title__contains=term)|Post.objects.filter(body__contains=term)
    return  render_to_response('blog/post_search.html',{'posts':posts,'term':term})

@login_required
def home(request):
    return render_to_response('blog/base.html',{'user':request.user}) 
