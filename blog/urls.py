from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/(<pk>\d+)/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/(<pk>\d+)/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('^post/(<pk>\d+)/publish/', views.post_publish, name='post_publish'),
    path('^post/(<pk>\d+)/remove/', views.post_remove, name='post_remove'),
]
