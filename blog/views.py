from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import BlogPost


class BlogPubPostListView(ListView):
    model = BlogPost
    paginate_by = 8
    template_name = 'blog_index.html'
    queryset = BlogPost.objects.all().filter(is_draft=False)
    context_object_name = 'list_of_pub_posts'



class BlogPubPostDetailView(DetailView):
    model = BlogPost
    template_name = 'post.html'
    context_object_name = 'post'
