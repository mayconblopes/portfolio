from django.shortcuts import render

from portfolio.models import About, Iam, Competence, Experience, Award


def index(request):
    about = About.objects.all().first()
    iam = Iam.objects.all().first()
    competences = Competence.objects.all()
    experiences = Experience.objects.all()
    awards = Award.objects.all()

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

        # Experiences Objects: attributes: name / where / when / description
        'experiences': experiences,

        # Awards Objects: attributes: who / description / link
        'awards': awards,
    }

    return render(request, 'index.html', context)
