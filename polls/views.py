from django.shortcuts import render

# Create your views here.

from .models import Post, Comment, User
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages

id = '###'

def home(request):
    if id == '###':
        return render(request, 'polls/login.html')
    else:
        return HttpResponseRedirect(reverse('index'))

def login(request):
    if User.objects.filter(u_id=request.POST['id']).count() == 1:
        user = User.objects.get(u_id=request.POST['id'])
        if user.u_passwd == request.POST['passwd']:
            return HttpResponseRedirect(reverse('index'))
    messages.success(request, "로그인실패")
    return HttpResponseRedirect(reverse('home'))

def register(request):
    return render(request, 'polls/register.html')

def register_do(request):
    if request.POST['passwd1'] != request.POST['passwd2']:
        raise Http404("입력한 패스워드가 다릅니다.")
    if User.objects.filter(u_id=request.POST['id']).count() == 1:
        raise Http404("존재하는 아이디입니다.")
    User.objects.create(u_id=request.POST['id'], u_passwd=request.POST['passwd1'])
#    global id = request.POST['id']
    return HttpResponseRedirect(reverse('index'))

def logout(request):
    return HttpResponseRedirect(reverse('home'))

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
    Post.objects.create(post_title=request.POST['post_title'], post_text=request.POST['post_text'], created_date=timezone.now())
    return HttpResponseRedirect(reverse('index'))

def comment(request, post_id):
    p = Post.objects.get(pk=post_id)
    p.comment_set.create(comment_text=request.POST['comment_text'], comment_date=timezone.now())
    return HttpResponseRedirect(reverse('detail', args=(p.id,)))

def remove(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('index'))
