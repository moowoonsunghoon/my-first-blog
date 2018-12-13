from django.shortcuts import render, redirect
from .models import *
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.db import models
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
def index(request):
    resume = Resume.objects.get()
    if request.method == "POST":
        form = CommentForm2(request.POST)   
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.resume = resume
            comment.save()
            return redirect('index')  #HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    else:
        form = CommentForm2()
    return render(request, 'blog/index.html', {'resume':resume, 'form':form} )

# post 잡담
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    #검색
    qs = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    q = request.GET.get('q', '')
    search_type = request.GET.get('type')
    us = User.objects.all()
    s1 = ''
    s2 = ''
    s3 = ''
    authorli = []
    m = 0
    n = 10
     #페이지수
    paginator = Paginator(posts, 20)
    page = request.GET.get('page', '1')
    contacts = paginator.get_page(page)
    paginators = posts
    #페이지수 일정범위만 표현하기
    if page:
        m += 10 * ((int(page)-1) // 10)
        n += 10 * ((int(page)-1) // 10)
    ranges = paginator.page_range[m:n]
    #검색    
    if search_type == 'title':
        qs = qs.filter(title__icontains=q).order_by('-published_date')
        paginator = Paginator(qs, 20)
        contacts = paginator.get_page(page)
        paginators = qs
        s1 = 'selected'

    elif search_type == 'titletext':
        qs = qs.filter(   
        Q(title__icontains=q) | Q(text__icontains=q)
        ).order_by('-published_date')
        paginator = Paginator(qs, 20)
        contacts = paginator.get_page(page)
        paginators = qs
        s2 = 'selected'

    elif search_type == 'author_id':
        us = us.filter(username__icontains=q)
        for i in us:
            user = qs.filter(author = i.pk).order_by('-published_date')
            authorli += user
        paginator = Paginator(authorli, 20)
        contacts = paginator.get_page(page)
        paginators = authorli
        s3 = 'selected'

    context = {
        'posts':posts, 
        #검색
        'qs':qs, 
        'q': q, 
        'us':us,
        's1':s1,
        's2':s2, 
        's3':s3, 
        'type':search_type, 
        'us':us, 
        'authorli':authorli,
        #페이지수 
        'contacts':contacts,
        'paginators':paginators,
        'ranges':ranges, #일정범위 표현
        }
    return render(request, 'blog/post_list.html', context)

@login_required
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', id)  #HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html',{'post':post, 'form':form})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

@login_required
def post_edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'post':post})

@login_required
def post_remove(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_remove.html', {'post' : post} )

#post 댓글삭제

@login_required
def comment_remove(request, id):
    comment = get_object_or_404(Comment, pk=id)
    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', comment.post.pk )
    return render(request, 'blog/post_comment_remove.html', {'comment' : comment})

@login_required
def comment2_remove(request, id):
    comment = get_object_or_404(Comment2, pk=id)
    if request.method == 'POST':
        comment.delete()
        return redirect('index')
    return render(request, 'blog/resume_comment_remove.html', {'comment' : comment})
#회원가입
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['repassword']:      
                new_user = User.objects.create_user(
                    username = form.cleaned_data['username'],
                    email = form.cleaned_data['email'],
                    password = form.cleaned_data['password'],
                    first_name = form.cleaned_data['first_name'],
                    last_name = form.cleaned_data['first_name'][0],
                    )
               
                login(request, new_user)
                return redirect('success')
    else:
        form = UserForm()
    return render(request, 'blog/signup.html', {'form': form,})

def success(request):
    return render(request, 'blog/success.html', {})


def member(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            logout(request)
            return redirect('member')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/member.html', {'form': form})

def resumeedit(request, id):
     resume = get_object_or_404(Resume, pk=id)
     if request.method == "POST":
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.save()
            return redirect('index')
     else:
        form = ResumeForm(instance=resume)
     return render(request, 'blog/resumeedit.html', {'form': form})