from django.urls import path

from blog.views import BlogPubPostListView

urlpatterns = [
    path('posts', BlogPubPostListView.as_view(), name='posts')

]