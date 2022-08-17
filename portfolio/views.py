from django.shortcuts import render

from portfolio.models import About, Iam, Competence, Experience, Award, Papper, PortfolioItem


def index(request):
    about = About.objects.all().first()
    iam = Iam.objects.all()
    competences = Competence.objects.all()
    experiences = Experience.objects.all()
    awards = Award.objects.all()
    pappers = Papper.objects.all()
    portfolio_items = PortfolioItem.objects.all()

    context = {

        # About Object attributes
        'about_title': about.title,
        'simple_description': about.simple_description,
        'more_description': about.more_description,

        # Iam Object
        'iam': iam[0],

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
    }

    return render(request, 'index.html', context)
