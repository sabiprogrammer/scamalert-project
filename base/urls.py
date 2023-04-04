from django.urls import path
from .views import (
    index, faq, about_us, 
    terms_and_conditions,
    )

app_name = 'base'

urlpatterns = [
    path('frequently-asked-questions/', faq, name='faq'),
    path('about-us/', about_us, name='about_us'),
    path('terms-and-conditions/', terms_and_conditions, name='terms_and_conditions'),
    path('', index, name='home'),
]


