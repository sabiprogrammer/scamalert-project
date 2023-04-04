from django.urls import path
from .views import share_your_story, my_reports, my_opinions, case_i_follow, shared_stories, story_details

app_name = 'scams'

urlpatterns = [
    path('share-your-story/', share_your_story, name='share-your-story'),
    path('my-reports/', my_reports, name='my-reports'),
    path('my-opinions/', my_opinions, name='my-opinions'),
    path('cases-i-follow/', case_i_follow, name='cases-i-follow'),
    path('shared-stories/', shared_stories, name='share_stories'),
    path('story/<slug:story_slug>/<uuid:story_pk>/', story_details, name='story-details'),
]
