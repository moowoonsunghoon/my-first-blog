from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
