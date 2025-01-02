from django.shortcuts import render

# Create your views here.


def home(request):
    context = {'key': "first message"}
    return render(request, 'main/home.html', context)