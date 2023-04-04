from django.urls import path
from .views import register, login_page, user_profile, logout_page

app_name = 'account'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_page, name='login_page'),
    path('profile/', user_profile, name='user-profile'),
    path('logout/', logout_page, name='logout'),
]