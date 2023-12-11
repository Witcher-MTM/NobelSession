from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import UserForm
def register_user(request):
    form = UserForm()
    context = {'form':form}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    return render(request, 'user/register_form.html', context)

# Create your views here.
