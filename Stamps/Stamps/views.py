from django.shortcuts import render

def inicio_proyecto(request):
    return render(request, 'index.html')