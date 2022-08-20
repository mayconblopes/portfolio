from django.shortcuts import render

from blog.views import BlogPubPostListView
from portfolio.models import About, Iam, Competence, Experience, Award, Papper, PortfolioItem


def index(request):
    about = About.objects.all().first()
    # iam = Iam.objects.all() -> this is not necessary anymore, because I've created a context processor for IAm object
    competences = Competence.objects.all()
    experiences = Experience.objects.all()
    awards = Award.objects.all()
    pappers = Papper.objects.all()
    portfolio_items = PortfolioItem.objects.all()
    latest_4_posts = BlogPubPostListView.queryset[:4]

    context = {

        # About Objects
        'about': about,

        # Iam Object
        # 'iam': iam[0],

        # Competences Objects
        'competences': competences,

        # Experiences Objects
        'experiences': experiences,

        # Awards Objects
        'awards': awards,

        # Pappers Objects
        'pappers': pappers,

        # PortfolioItems Objects
        'portfolio_items': portfolio_items,

        'latest_4_posts': latest_4_posts,
    }

    return render(request, 'index.html', context)
