
from django.http import HttpResponse
from django.shortcuts import render

def familiar_1 (request):
    return HttpResponse ('F_1')

def Fam_1(request):
    context = {
        'nombre':'Maxi',
        'apellido':'Rivera',
        'prueba':'1234',
        'frutas':['asd', 'dfgdfg', '243423423']
    }
    return render(request, 'template_1.html', context = context)






