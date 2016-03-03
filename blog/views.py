from django.shortcuts import render

# Create your views here.

def index(request):

    data = {'mydata': "Heloo hello"}
    return render(request, 'blog/index.html', data)

def home(request):

    data = {'mydata': "home home home"}
    return render(request, 'blog/home.html', data)