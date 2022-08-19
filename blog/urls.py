from django.urls import path

from blog import views
from blog.views import BlogPubPostListView

urlpatterns = [
    path('posts', BlogPubPostListView.as_view(), name='posts'),
    path('', views.blog_index, name='blog_index'),

]