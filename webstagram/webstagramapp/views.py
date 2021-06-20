from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Content

# Create your views here.

def feed(request, id):
    contents=get_object_or_404(Content,pk=id)
    return render(request, 'feed.html', {'post':contents})

