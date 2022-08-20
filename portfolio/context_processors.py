from portfolio.models import Iam


def iam_processor(request):
    """
    Turn IAm objects available for all templates
    """

    iam = Iam.objects.all().first()
    context = {'iam': iam}

    return context
