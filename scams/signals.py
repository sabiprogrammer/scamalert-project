from django.dispatch import receiver
from django.db.models.signals import post_delete

from .models import SharedStoriesModel


@receiver(post_delete, sender=SharedStoriesModel)
def delete_story_scammer_picture(sender, instance, *args, **kwargs):
    print("Hello")
    if instance.scammer_profile_pic:
        print("YES")
        instance.scammer_profile_pic.delete(save=False)
    else:
        print("NO")
