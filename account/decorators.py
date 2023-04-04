from django.shortcuts import redirect
from django.contrib import messages

def user_not_logged_in(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, "You are already logged in")
            return redirect('base:home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
