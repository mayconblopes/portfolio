from django.urls import path

from blog import views
from blog.views import BlogPubPostListView, BlogPubPostDetailView

urlpatterns = [
    path('', BlogPubPostListView.as_view(), name='blog_index'),
    path('<slug:slug>', BlogPubPostDetailView.as_view(), name='post_detail'),

]