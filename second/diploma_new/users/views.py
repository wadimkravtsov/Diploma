from django.shortcuts import render
from django.shortcuts import render, redirect
# from .models import Profile, Message
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, "Username does not exist")
            # print("Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('villages')
        else:
            messages.info(request, "User was logged out!")
            # print("Username or password is incorrect")
    return render(request, "users/login_user.html")

def logout_user(request):
    logout(request)
    messages.info(request, "User was logged out!")
    return redirect('login')
    # return render(request, "users/logout_user.html")

def register_user(request):
    form = CustomUserCreationForm
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account was created!")
            login(request, user)
            return redirect('villages')
        else:
            messages.error(request, "An error has occurred during registration")
    context = {
        # 'page': page,
        'form': form
    }
    return render(request, "users/register_user.html", context)

@login_required(login_url='login')
def profile(request):
    prof = request.user.profile
    print(prof)
    context = {
        "profile": prof
    }

    return render(request, "users/profile.html", context)

@login_required(login_url='login')
def edit_profile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {
        'form': form
    }
    return render(request, 'users/profile_form.html', context)

