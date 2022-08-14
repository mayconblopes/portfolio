from django.shortcuts import render

from portfolio.models import About, Iam, Competence, Experience


def index(request):
    about = About.objects.all().first()
    iam = Iam.objects.all().first()
    competences = Competence.objects.all()
    experiences = Experience.objects.all()

    context = {

        # About Object attributes
        'about_title': about.title,
        'simple_description': about.simple_description,
        'more_description': about.more_description,

        # I Am Object attributes
        'hello_msg': iam.hello_msg,
        'name': iam.name,
        'featured_skills': iam.featured_skills,

        # Competences Objects: attributes: icon / name / description
        'competences': competences,

        # Experiences Objects: attributes: icon / name / description
        'experiences': experiences,
    }

    return render(request, 'index.html', context)
