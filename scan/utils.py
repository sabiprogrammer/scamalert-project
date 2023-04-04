from django.db.models import Q
from .models import (BankDetailSearchModel,
                     FullnameSearchModel,
                     WebsiteUrlSearchModel,
                     CompanyNameSearchModel,
                     PhoneNumberSearchModel)

from scams.models import SharedStoriesModel

def save_search(request, searched_field, model):
    content = request.GET.get(searched_field).lower().strip()
    object, created = model.objects.get_or_create(
        content=content,
    )
    object.user.add(
        request.user) if request.user.is_authenticated else object.user.add(None)
    object.times_searched = object.times_searched + 1
    object.save()


def save_bank_search(request):
    bank_name = request.GET.get("bank-name").lower().strip()
    account_number = request.GET.get("account-number").strip()
    object, created = BankDetailSearchModel.objects.get_or_create(
        bank_name=bank_name,
        account_number=account_number
    )
    object.user.add(
        request.user) if request.user.is_authenticated else object.user.add(None)
    object.times_searched = object.times_searched + 1
    object.save()

def get_search_details(request):
    result = None
    what_searched = ""
    what_searched_value = ""
    searched_field = (request.GET['search-website'] or
                        request.GET['search-bank'] or
                        request.GET['search-company'] or
                        request.GET['search-phone'] or
                      request.GET['search-fullname']).strip()
    
    # handling what happens when a bank detail is searched
    if searched_field == 'bank':
        account_number = request.GET.get('account-number').strip()
        bank_name = request.GET.get('bank-name').strip()
        what_searched = 'account number'
        what_searched_value = account_number

        if account_number and bank_name:
            result = SharedStoriesModel.objects.filter(
                scammer_account_number__icontains=account_number,
                scammer_bank_name__icontains=bank_name
            )
        elif account_number:
            result = SharedStoriesModel.objects.filter(
                scammer_account_number__icontains=account_number,
            )
        elif bank_name:
            result = SharedStoriesModel.objects.filter(
                scammer_bank_name__icontains=bank_name
            )
            what_searched = 'bank'
            what_searched_value = bank_name
        
        # save search to database
        save_bank_search(request)

    # handling what happens when a fullname is searched
    if searched_field == 'fullname':
        fullname_value = request.GET.get(searched_field).strip()
        what_searched = "name"
        what_searched_value = fullname_value
        result = SharedStoriesModel.objects.filter(
            Q(scammer_fullname_or_website__icontains=fullname_value) |
            Q(scammer_othernames_nickname__icontains=fullname_value)
        )

        # save search to database
        save_search(request, searched_field, FullnameSearchModel)

    # handling what happens when a website url is searched
    if searched_field == 'website':
        website_address = request.GET.get(searched_field).strip()
        what_searched = "website address"
        what_searched_value = website_address
        result = SharedStoriesModel.objects.filter(
            Q(scammer_fullname_or_website__icontains=website_address) |
            Q(scammer_website_or_group_link__icontains=website_address)
        )

        # save search to database
        save_search(request, searched_field, WebsiteUrlSearchModel)

    # handling what happens when a company name is searched
    if searched_field == 'company':
        company_name = request.GET.get(searched_field).strip()
        what_searched = "company name"
        what_searched_value = company_name
        result = SharedStoriesModel.objects.filter(
            Q(scammer_fullname_or_website__iexact=company_name) |
            Q(scammer_website_or_group_link__icontains=company_name) |
            Q(scammer_othernames_nickname__iexact=company_name)
        )

        # save search to database
        save_search(request, searched_field, CompanyNameSearchModel)

    # handling what happens when a phone number is searched
    if searched_field == 'phone':
        phone_number = request.GET.get(searched_field).strip()
        what_searched = "phone number"
        what_searched_value = phone_number
        result = SharedStoriesModel.objects.filter(
            Q(scammer_phone_number__iexact=phone_number)
        )

        # save search to database
        save_search(request, searched_field, PhoneNumberSearchModel)

    return {
        'result': result,
        'what_searched': what_searched,
        'what_searched_value': what_searched_value
    }
