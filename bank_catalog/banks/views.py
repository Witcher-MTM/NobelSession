from django.shortcuts import render, redirect
from .models import Bank
from .forms import BankForm
def index(req):
    banks = Bank.objects.all()
    print(banks)
    data = {
        'title': 'Banks2',
        'banks': banks
    }
    return render(req, 'banks/banks_index.html', data)


def AddBank(req):
    error = ''
    if req.method == 'POST':
        form = BankForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('banks')
        else:
            error = 'invalid form data'

    form = BankForm()

    data = {
        'title': 'Create Bank',
        'form':form,
        'error':error
    }
    return render(req, 'banks/banks_create.html', data)