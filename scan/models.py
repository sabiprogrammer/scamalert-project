from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class BankDetailSearchModel(models.Model):
    user = models.ManyToManyField(User, blank=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    account_number = models.CharField(max_length=25, blank=True, null=True)
    times_searched = models.PositiveIntegerField(default=0)
    date_searched = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('bank_name', 'account_number')

    def __str__(self):
        return f"{self.bank_name} - {self.account_number}"


class FullnameSearchModel(models.Model):
    user = models.ManyToManyField(User, blank=True)
    content = models.CharField(max_length=255, blank=True, null=True, unique=True)
    times_searched = models.PositiveIntegerField(default=0)
    date_searched = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class WebsiteUrlSearchModel(models.Model):
    user = models.ManyToManyField(User, blank=True)
    content = models.CharField(max_length=255, blank=True, null=True, unique=True)
    times_searched = models.PositiveIntegerField(default=0)
    date_searched = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class CompanyNameSearchModel(models.Model):
    user = models.ManyToManyField(User, blank=True)
    content = models.CharField(max_length=255, blank=True, null=True, unique=True)
    times_searched = models.PositiveIntegerField(default=0)
    date_searched = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class PhoneNumberSearchModel(models.Model):
    user = models.ManyToManyField(User, blank=True)
    content = models.CharField(max_length=25, blank=True, null=True, unique=True)
    times_searched = models.PositiveIntegerField(default=0)
    date_searched = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
