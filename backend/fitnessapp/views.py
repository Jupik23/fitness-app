from django.shortcuts import render

def firstpage(request):
    return render(request, 'firstpage/firstpage.html')