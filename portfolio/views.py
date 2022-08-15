from django.shortcuts import render

from portfolio.models import About, Iam, Competence, Experience, Award, Papper


def index(request):
    about = About.objects.all().first()
    iam = Iam.objects.all().first()
    competences = Competence.objects.all()
    experiences = Experience.objects.all()
    awards = Award.objects.all()
    pappers = Papper.objects.all()

    context = {

        # About Object attributes
        'about_title': about.title,
        'simple_description': about.simple_description,
        'more_description': about.more_description,

        # Iam Object attributes
        'hello_msg': iam.hello_msg,
        'name': iam.name,
        'featured_skills': iam.featured_skills,

        # Competences Objects
        'competences': competences,

        # Experiences Objects
        'experiences': experiences,

        # Awards Objects
        'awards': awards,

        # Pappers Objects
        'pappers': pappers,
    }

    return render(request, 'index.html', context)
