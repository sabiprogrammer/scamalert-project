# Generated by Django 4.1.6 on 2023-04-04 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import scams.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SharedStoriesModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_victim', models.CharField(choices=[('The victim', 'The victim'), ('Reporting for a victim', 'Reporting for a victim'), ('Reporting on behalf of a company', 'Reporting on behalf of a company'), ('I am a witness', 'I am a witness')], default=None, max_length=100, null=True)),
                ('is_anonymous', models.CharField(choices=[('0', 'I wish to remain anonymous'), ('1', 'I do not mind sharing my profile')], default=None, max_length=100, null=True)),
                ('who_are_you_reporting', models.CharField(blank=True, max_length=100, null=True)),
                ('which_information_do_you_have', models.CharField(blank=True, max_length=100, null=True)),
                ('scammer_fullname_or_website', models.CharField(blank=True, max_length=255, null=True)),
                ('scammer_gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default=None, max_length=10, null=True)),
                ('scammer_age_range', models.CharField(choices=[('5-14', '5-14'), ('15-25', '15-25'), ('26-35', '26-35'), ('36-45', '36-45'), ('46-55', '46-55'), ('56-65', '56-65'), ('66+', '66 and above')], default=None, max_length=10, null=True)),
                ('scammer_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('scammer_bank_name', models.CharField(blank=True, max_length=255, null=True)),
                ('scammer_account_number', models.CharField(blank=True, max_length=255, null=True)),
                ('scammer_othernames_nickname', models.CharField(blank=True, max_length=255, null=True)),
                ('scammer_profession', models.CharField(blank=True, max_length=255, null=True)),
                ('scammer_website_or_group_link', models.CharField(blank=True, max_length=255, null=True)),
                ('scammer_profile_pic', models.ImageField(blank=True, default='scampictures/avatar.png', max_length=1000, null=True, upload_to=scams.models.upload_location)),
                ('describe_what_happened', models.TextField()),
                ('scam_evidence', models.ImageField(blank=True, default='', null=True, upload_to=scams.models.upload_location)),
                ('loss_suffered', models.CharField(blank=True, max_length=100, null=True)),
                ('info_to_public', models.TextField()),
                ('agreement', models.BooleanField(default=False)),
                ('date_reported', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('modified_img', models.CharField(blank=True, max_length=255, null=True)),
                ('modified_user_pic', models.TextField(blank=True, null=True)),
                ('modified_username', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OpinionsDropped',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_dropped', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('story', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='scams.sharedstoriesmodel')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]