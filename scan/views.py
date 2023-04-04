from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q

from scams.models import SharedStoriesModel

from .models import (BankDetailSearchModel,
                     FullnameSearchModel,
                     WebsiteUrlSearchModel,
                     CompanyNameSearchModel,
                     PhoneNumberSearchModel)

from .utils import get_search_details


User = get_user_model()
# admin_user = User.objects.get(id=1)

def check_identity(request):
    return render(request, 'scan/check_identity.html', {})

def process_scan(request):
    feedback = get_search_details(request)
    context = {
        'result': feedback['result'],
        'what_searched': feedback['what_searched'],
        'what_searched_value': feedback['what_searched_value'],
    }

    if not feedback['what_searched']:
        messages.warning(request, 'please click the verify button to search')
        return redirect('scan:check-identity')
    
    return render(request, 'scan/scan_result.html', context)
    
