import uuid
from PIL import Image
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.template.defaultfilters import slugify

User = settings.AUTH_USER_MODEL


def upload_location(instance, filename, *args, **kwargs):
    file_path = 'scampictures/{user_id}/{filename}'.format(
        user_id=str(instance.user.id), filename=filename)
    return file_path


class SharedStoriesModel(models.Model):
    IS_VICTIM_CHOICES = (
        ('The victim', 'The victim'),
        ('Reporting for a victim', 'Reporting for a victim'),
        ('Reporting on behalf of a company', 'Reporting on behalf of a company'),
        ('I am a witness', 'I am a witness'),
    )
    IS_ANONYMOUS_CHOICES = (
        ('0', 'I wish to remain anonymous'),
        ('1', 'I do not mind sharing my profile'),
    )

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    AGE_RANGE_CHOICES = (
        ('5-14', '5-14'),
        ('15-25', '15-25'),
        ('26-35', '26-35'),
        ('36-45', '36-45'),
        ('46-55', '46-55'),
        ('56-65', '56-65'),
        ('66+', '66 and above'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    is_victim = models.CharField(
        max_length=100, choices=IS_VICTIM_CHOICES, blank=False, null=True, default=None)
    is_anonymous = models.CharField(
        max_length=100, choices=IS_ANONYMOUS_CHOICES, blank=False, null=True, default=None)
    who_are_you_reporting = models.CharField(
        max_length=100, blank=True, null=True)
    which_information_do_you_have = models.CharField(
        max_length=100, blank=True, null=True)

    # step 5 of the form
    scammer_fullname_or_website = models.CharField(
        max_length=255, blank=True, null=True)
    scammer_gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, blank=False, null=True, default=None)
    scammer_age_range = models.CharField(
        max_length=10, choices=AGE_RANGE_CHOICES, blank=False, null=True, default=None)
    scammer_phone_number = models.CharField(
        max_length=20, blank=True, null=True)
    scammer_bank_name = models.CharField(max_length=255, blank=True, null=True)
    scammer_account_number = models.CharField(
        max_length=255, blank=True, null=True)
    scammer_othernames_nickname = models.CharField(
        max_length=255, blank=True, null=True)
    scammer_profession = models.CharField(
        max_length=255, blank=True, null=True)
    scammer_website_or_group_link = models.CharField(
        max_length=255, blank=True, null=True)
    scammer_profile_pic = models.ImageField(
        default='scampictures/avatar.jpg', blank=True, null=True, upload_to=upload_location, max_length=1000)

    # step 6 of the form
    describe_what_happened = models.TextField(blank=False, null=False)

    # step 7 of the form
    scam_evidence = models.ImageField(
        default='', blank=True, null=True, upload_to=upload_location)

    # step 8 of the form
    loss_suffered = models.CharField(max_length=100, blank=True, null=True)

    # step 9 of the form
    info_to_public = models.TextField(blank=False, null=False)

    # step 10 of the form
    agreement = models.BooleanField(default=False)

    date_reported = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    modified_img = models.CharField(max_length=255, blank=True, null=True)
    modified_user_pic = models.TextField(null=True, blank=True)
    modified_username = models.CharField(max_length=255, blank=True, null=True)


    def get_who_are_you_reporting(self):
        return self.who_are_you_reporting.split(',')  # ignore

    def get_which_information_do_you_have(self):
        return self.which_information_do_you_have.split(',')

    def get_loss_suffered(self):
        return [self.loss_suffered.split(',')]

    def __str__(self):
        return f"{self.user}'s story"

    def get_absolute_url(self):
        return reverse("scams:story-details", kwargs={
            "story_slug": slugify(self.info_to_public[:100]),
            "story_pk": self.pk,
        })

    # reduce the size of the scammer profile image if it's more than 900px
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.scammer_profile_pic:
            img = Image.open(self.scammer_profile_pic.path)
            if img.height > 500 or img.width > 1000:
                output = (500, 900)
                img.thumbnail(output)
                img.save(self.scammer_profile_pic.path)

        if self.scam_evidence:
            img = Image.open(self.scam_evidence.path)
            if img.height > 900 or img.width > 1500:
                output = (900, 1500)
                img.thumbnail(output)
                img.save(self.scam_evidence.path)

    @property
    def get_scammer_pic(self):
        return self.scammer_profile_pic.url

    @property
    def get_scam_evidence(self):
        return self.scam_evidence.url


class OpinionsDropped(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=True, blank=True)
    story = models.ForeignKey(
        SharedStoriesModel, on_delete=models.DO_NOTHING, null=True, blank=True)
    comment = models.TextField()

    date_dropped = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
