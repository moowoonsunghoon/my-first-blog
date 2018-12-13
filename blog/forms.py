from django import forms
from django.contrib.auth.models import User
from .models import *

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length = 100, label = '제목')
    text = forms.CharField(widget=forms.Textarea, label='내용')
    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class' : 'cominput', 'placeholder': '댓글을 입력하세요. 최대 300자'}), max_length = 300, label='')
    class Meta:
        model = Comment
        fields = ('text',)

class CommentForm2(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class' : 'cominput', 'placeholder': '저를 채용해가실 회사는 댓글을 남겨주세요.\n모든 글은 비밀글로 작성됩니다.'}), max_length = 300, label='')
    class Meta:
        model = Comment2
        fields = ('text',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label = '비밀번호', min_length= 8, max_length=20)
    repassword = forms.CharField(widget=forms.PasswordInput(), label = '비밀번호확인', min_length= 8, max_length=20)
    first_name = forms.CharField(label='이름')
    email = forms.CharField(widget=forms.EmailInput, label = '이메일')
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password', 'repassword']

class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ('photo', 'name', 'birth', 'email', 'number', 'education', 'career', 'introduce', 'portfolio')