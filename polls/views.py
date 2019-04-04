from django.shortcuts import render

# Create your views here.

from .models import Post,Comment
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

def index(request):
    post_list = Post.objects.order_by('-created_date')[:]
    context = {
        'post_list' : post_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    comment = post.comment_set.all()
    context = {
        'post' : post,
        'comment' : comment,
    }
    return render(request, 'polls/detail.html', context)

def modify(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.post_title = request.POST['post_title']
    post.post_text = request.POST['post_text']
    post.save()
    return HttpResponseRedirect(reverse('detail', args=(post.id,)))

def new(request):
    return render(request, 'polls/new.html')

def create(request):
    Post.objects.create(post_title=request.POST['post_title'], post_text=request.POST['post_text'], create_date=timezone.now())
    return HttpResponseRedirect(reverse('index'))

def comment(request, post_id):
    p = Post.objects.get(pk=post_id)
    p.comment_set.create(comment_text=request.POST['comment_text'], comment_date=timezone.now())
    return HttpResponseRedirect(reverse('detail', args=(p.id,)))
