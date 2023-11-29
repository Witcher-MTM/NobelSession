from django.shortcuts import render
from .models import Bank
def index(req):
    banks = Bank.objects.all()
    print(banks)
    data = {
        'title': 'Banks2',
        'banks': banks
    }
    return render(req, 'banks/banks_index.html', data)
