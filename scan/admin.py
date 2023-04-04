from django.contrib import admin

from .models import *

admin.site.register(BankDetailSearchModel)
admin.site.register(FullnameSearchModel)
admin.site.register(WebsiteUrlSearchModel)
admin.site.register(CompanyNameSearchModel)
admin.site.register(PhoneNumberSearchModel)
