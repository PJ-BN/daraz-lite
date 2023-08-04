from django.shortcuts import render, redirect

# Create your views here.

def landing(request):
    context = {
        "data" : [1,2,3,4,5,6,7,8,9,10]
    }
    return render(request, 'landing.html', context)


def home(request):
    context = {
        "data" : [1,2,3,4,5,6,7,8,9,10]
    }
    return render(request, 'home.html', context)

def profile(request):
    if request.method =='GET':
        return render(request, 'profile.html')