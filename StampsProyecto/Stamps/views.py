from django.shortcuts import render
from AppBlog.views import carga_avatar
def inicio_proyecto(request):
    return render(request, 'Stamps/templates/index.html')

def about_us(request):
    return render(request, 'about.html', {'imagen':carga_avatar(request)})