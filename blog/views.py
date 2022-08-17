from django.shortcuts import render
from django.views.generic import ListView

from blog.models import BlogPost


class BlogPubPostListView(ListView):
    model = BlogPost
    queryset = BlogPost.objects.all().filter(is_draft=False)
    context_object_name = 'list_of_pub_posts'
