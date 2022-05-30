from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from familia_app.models import familia



# Create your views here.

def familiares(request):
    fam_1 = familia.objects.create(
        nombre='Jose',
        apellido='Rivera',
        dni='11111111',
        estado='Casado',
        fecha='10/05/1954'
    )
    
    fam_2 = familia.objects.create (
        nombre='Lola',
        apellido='Miño',
        dni='222222222',
        estado='Casada',
        fecha='12/03/1955')
    
    fam_3 = familia.objects.create (
        nombre='Axel',
        apellido='Rivera Miño',
        dni='33333333',
        estado='Soltero',
        fecha='25/10/1999')
    

    context =  {'fam_1':fam_1, 'fam_2':fam_2,'fam_3':fam_3}
    return render(request, 'template_1.html', context=context)







