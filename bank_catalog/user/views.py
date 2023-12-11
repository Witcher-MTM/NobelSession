from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
def register_user(req):
    form = UserCreationForm(req.POST)
    context = {'from':form}
    return render(req, 'user/register_form.html', context)

# Create your views here.
