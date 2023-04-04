from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.serializers import serialize
from django.http import JsonResponse
from django.contrib import messages

from .models import SharedStoriesModel
from .forms import SharedStoriesForm
from .utils import db_string_to_list

import json

@login_required()
def share_your_story(request):
    form = SharedStoriesForm(request.POST or None)
    if request.method == 'POST':
        form = SharedStoriesForm(request.POST, request.FILES)
        if form.is_valid():
            story = form.save(commit=False)
            story.user = request.user

            story.save()
            
            # create a new url for pic to send to js
            scammer_pic = request.build_absolute_uri(f'/media/{story.scammer_profile_pic}')
            story.modified_img = scammer_pic

            # create a new image url for user pic to send to js
            modified_user_pic = request.build_absolute_uri(
                f'{story.user.user_profile.get_image_url}')
            story.modified_user_pic = modified_user_pic

            # saving the username
            modified_username = story.user.user_profile.full_name
            story.modified_username = modified_username
            
            story.save()
            messages.success(request, 'Thank you for sharing that story with the public')
            return redirect("account:user-profile")
        else:
            print('ERRORS: ', form.errors)
            messages.error(request, 'An error occured while submitting your form. Please try again')

    return render(request, 'scams/report.html', {'form': form})


@login_required()
def my_reports(request):
    my_stories = SharedStoriesModel.objects.filter(user=request.user)
    context = {
        'my_stories': my_stories,
    }
    return render(request, 'scams/my_reports.html', context)


@login_required()
def my_opinions(request):
    my_opinions = SharedStoriesModel.objects.filter(user=request.user) #query from opinion model
    context = {
        'my_opinions': my_opinions,
    }
    return render(request, 'scams/my_opinions.html', context)


@login_required()
def case_i_follow(request):
    my_cases = SharedStoriesModel.objects.filter(user=request.user) #query from opinion model
    context = {
        'my_cases': my_cases,
    }
    return render(request, 'scams/my_cases.html', context)


def shared_stories(request):
    # ajax = request.headers
    # print("AJAX ", ajax)

    # processing the "load more button" via javascript
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        post_count = int(json.load(request)['postCount'])
        
        stories = SharedStoriesModel.objects.all().order_by("-date_reported")[post_count:post_count + 3]
        print("S: ", stories)
        result = {
            'stories': serialize("json", stories),
            'post_count': post_count,
        }
        return JsonResponse(result)
    else:
        post_count = 3
        stories = SharedStoriesModel.objects.all().order_by("-date_reported")[:post_count]

        context = {
            'stories': stories,
        }

        return render(request, 'scams/some_shared_stories.html', context)


def story_details(request, story_slug, story_pk):
    story = get_object_or_404(SharedStoriesModel, pk=story_pk)
    loss_suffered = db_string_to_list(story.loss_suffered)
    
    context = {
        'story': story,
        'loss_suffered': loss_suffered,
    }
    print("L: ", loss_suffered)
    return render(request, 'scams/single_story_detail.html', context)
