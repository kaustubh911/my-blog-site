from django.shortcuts import render

def myHome(request):
    return render(request, 'homePage.html')

def myContact(request):
    return render(request, 'contactPage.html')
