from django.shortcuts import render

def weatherhome(request):
    return render(request, 'weatherhome.html', {})

def about(request):
    return render(request, 'about.html', {})