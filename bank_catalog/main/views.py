from django.shortcuts import render

def index(req):
    data = {
        'title':'Title data'
    }
    return render(req, 'main/index.html', data)
