from . import views
from django.urls import include, path

urlpatterns = [
    #post
    path('', views.index, name='index'),
    path('post/', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:id>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:id>/remove/', views.post_remove, name='post_remove'),
    #post 댓글
    path('comment/<int:id>/remove/', views.comment_remove, name='comment_remove'),
    path('comment2/<int:id>/remove/', views.comment2_remove, name='comment2_remove'),
    #회원가입
    path('signup/', views.signup, name='signup'),
    path('success/', views.success, name ='success'),
    #비밀번호 변경
    path('member/', views.member, name='member'),
    #이력서 수정
    path('<int:id>/resumeedit', views.resumeedit, name='resumeedit'),
]
