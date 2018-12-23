from django.shortcuts import render

def myBlog(request):
    return render(request, 'blogPage.html')
