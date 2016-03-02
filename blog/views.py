from django.shortcuts import render

# Create your views here.

def index(request):

    data = {'mydata': "Heloo hello"}
    return render(request, 'blog/index.html', data)