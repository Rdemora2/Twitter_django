from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from apps.notification.utilities import create_notification

from .forms import profileForm

def profile(request, username):
    user = get_object_or_404(User, username=username)
    oinks = user.oinks.all()

    for oink in oinks:
        likes = oink.likes.filter(created_by_id=request.user.id)

        if likes.count() > 0:
            oink.liked = True
        else:
            oink.liked = False

    context = {
        'user': user,
        'oinks': oinks
    }

    return render(request, 'profile/profile.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()

            return redirect('profile', username=request.user.username)
    else:
        form = profileForm(instance=request.user.profile)
    
    context = {
        'user': request.user,
        'form': form
    }

    return render(request, 'profile/edit_profile.html', context)

@login_required
def follow(request, username):
    user = get_object_or_404(User, username=username)

    request.user.profile.follows.add(user.profile)

    create_notification(request, user, 'follower')

    return redirect('profile', username=username)

@login_required
def unfollow(request, username):
    user = get_object_or_404(User, username=username)

    request.user.profile.follows.remove(user.profile)

    return redirect('profile', username=username)

def followers(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'profile/followers.html', {'user': user})

def follows(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'profile/follows.html', {'user': user})