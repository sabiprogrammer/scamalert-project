from django.shortcuts import render

from scams.models import SharedStoriesModel

def index(request):
    # bring up a better query model for this
    stories = SharedStoriesModel.objects.all()[:6]

    context = {
        'stories': stories,
    }
    return render(request, 'base/index.html', context)


def faq(request):
    return render(request, 'base/faq.html')


def about_us(request):
    return render(request, 'base/about_us.html')


def terms_and_conditions(request):
    return render(request, 'base/terms_and_conditions.html')
