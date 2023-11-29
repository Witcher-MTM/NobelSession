from django.shortcuts import render

def index(req):
    data = {
        'title':'Title data'
    }
    return render(req, 'banks/index.html', data)
