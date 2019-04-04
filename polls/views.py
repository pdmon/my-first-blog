from django.shortcuts import render

# Create your views here.

from .models import Post, Comment, User
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages


def home(request):
    if not 'id' in request.session:
        return render(request, 'polls/login.html')
    else:
        return HttpResponseRedirect(reverse('index'))

def login(request):
    if User.objects.filter(u_id=request.POST['id']).count() == 1:
        user = User.objects.get(u_id=request.POST['id'])
        if user.u_passwd == request.POST['passwd']:
            request.session['id'] = user.u_id
            return HttpResponseRedirect(reverse('index'))
    messages.error(request, "로그인실패")
    return HttpResponseRedirect(reverse('home'))

def register(request):
    return render(request, 'polls/register.html')

def register_do(request):
    if request.POST['passwd1'] != request.POST['passwd2']:
        raise Http404("입력한 패스워드가 다릅니다.")
    if User.objects.filter(u_id=request.POST['id']).count() == 1:
        raise Http404("존재하는 아이디입니다.")
    User.objects.create(u_id=request.POST['id'], u_passwd=request.POST['passwd1'])
    request.session['id'] = request.POST['id']
    return HttpResponseRedirect(reverse('index'))

def logout(request):
    if 'id' in request.session:
        del request.session['id']
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
    s_id = request.session['id']
    if s_id == post.post_author or s_id == 'admin':
        messages.error(request, "수정되었습니다.")
        post.save()
    else:
        messages.error(request, "수정할 수 없습니다.")
    return HttpResponseRedirect(reverse('detail', args=(post.id,)))

def new(request):
    return render(request, 'polls/new.html')

def create(request):
    s_id = request.session['id']
    Post.objects.create(post_title=request.POST['post_title'], post_text=request.POST['post_text'], created_date=timezone.now(), post_author=s_id)
    return HttpResponseRedirect(reverse('index'))

def comment(request, post_id):
    p = Post.objects.get(pk=post_id)
    s_id = request.session['id']
    p.comment_set.create(comment_text=request.POST['comment_text'], comment_date=timezone.now(), comment_author=s_id)
    return HttpResponseRedirect(reverse('detail', args=(p.id,)))

def remove(request, post_id):
    post = Post.objects.get(pk=post_id)
    s_id = request.session['id']
    if s_id == post.post_author or s_id == 'admin':
        post.delete()
        return HttpResponseRedirect(reverse('index'))
    else:
        messages.error(request, "삭제할 수 없습니다.")
        return HttpResponseRedirect(reverse('detail', args=(post_id,)))
