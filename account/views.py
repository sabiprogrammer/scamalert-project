from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect,get_object_or_404

from .models import Profile
from .decorators import user_not_logged_in
from .forms import UserRegisterForm, UserProfileRegisterForm, UserProfileUpdateForm, UserUpdateForm
User = get_user_model()


@user_not_logged_in
def register(request):
    form = UserRegisterForm(request.POST or None)
    profile_form = UserProfileRegisterForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            user_profile = profile_form.save(commit=False)
            user_profile.user = user
            user_profile.save()

            messages.success(request, 'Registration Sucessful. Please Login...')
            return redirect('account:login_page')
        else:
            # print("EERRORS: ", form.errors)
            # print("EERRORS: ", form.errors.as_data())
            messages.error(request, 'Email already taken!')

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'account/register.html', context)


@user_not_logged_in
def login_page(request):
    email = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)

            # checking the appropriate page to direct the user after login
            if request.GET.get('next'):
                messages.success(request, 'Login Sucessful! Please continue...')
                return redirect(request.GET.get("next"))
            else:
                messages.success(request, 'Login Sucessful. Welcome to your dashboard!')
                return redirect('account:user-profile')
        else:
            messages.warning(request, "Your email or password seems incorrect")

    return render(request, 'account/login.html', {'email': email})


@login_required()
def logout_page(request):
    messages.info(request, "logout successful")
    logout(request)
    return redirect("base:home")
    

@login_required()
def user_profile(request):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    profile_form = UserProfileUpdateForm(
        request.POST or None, request.FILES or None, instance=user_profile)
    user_form = UserUpdateForm(request.POST or None, instance=user)

    if request.method == 'POST':
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # user_profile = profile_form.save(commit=False)
            # user_profile.user = user
            user_profile.save()

            messages.success(
                request, 'Profile edit Sucessful!')
            return redirect('account:user-profile')
        else:
            messages.error(request, 'An error occured while updating your profile...')

    context = {
        'user': user,
        'profile': user_profile,
        'profile_form': profile_form,
        'user_form': user_form,
    }
    return render(request, 'dashboard/user_profile.html', context)
