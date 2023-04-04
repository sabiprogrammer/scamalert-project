from django.urls import path
from .views import check_identity, process_scan

app_name = 'scan'

urlpatterns = [
    path('check-identity/', check_identity, name='check-identity'),
    path('result/', process_scan, name='process-scan'),
]