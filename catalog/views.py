from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    context = {
        "data" : [1,2,3,4,5,6,7,8,9,10]
    }
    return render(request, 'landing.html', context)
