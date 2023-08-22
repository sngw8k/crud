from django.shortcuts import render, redirect

# Post 모델을 import
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'index.html', context)

def detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }

    return render(request, 'detail.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content =  request.GET.get('content')

    post = Post()
    post.title = title
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}/')

def delete(request, id):
    # 지우고 싶은 게시물 찾기
    post = Post.objects.get(id=id)
    # 지우기
    post.delete()

    # 삭제 후 메인 페이지로 이동
    return redirect('/index/')

def edit(request, id):
    # 수정하기 위해 기존 정보 가지고 오기
    post = Post.objects.get(id=id)

    context = {
        'post': post
    }

    return render(request, 'edit.html', context)

def update(request, id):
    # 기존 데이터
    post = Post.objects.get(id=id)

    # 방금 수정한 데이터
    title = request.GET.get('title')
    content = request.GET.get('content')

    # post = Post()  => 새로운 게시물 만들 떄
    # 기존데이터에 덮어씌우기
    post.title = title
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}/')