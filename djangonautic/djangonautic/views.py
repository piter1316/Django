# from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    # return HttpResponse('homepage')
    return render(request, 'homePage.html')


def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')