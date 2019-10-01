from __future__ import unicode_literals

from django.shortcuts import render
from .models import User
# Create your views here.

def displayUsers(request):
    myUsers = User.objects.all()
    context = { 'users' : myUsers}
    return render(request, 'myusers/DisplayUsers.html', context)

def displayDetails(request, id):
    myUser = User.objects.get(id = id)
    return render(request, 'myusers/DisplayOnlyOneUser.html', {'user': myUser})
