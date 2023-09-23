from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.


def student(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            Sname=SFDO.cleaned_data['Sname']
            Sage=SFDO.cleaned_data['Sage']
            Sid=SFDO.cleaned_data['Sid']
            Email=SFDO.cleaned_data['Email']
            SO=Student.objects.get_or_create(Sname=Sname,Sage=Sage,Sid=Sid,Email=Email)[0]
            SO.save()
            QSSO=Student.objects.all()
            d1={'QSSO':QSSO}
            return render(request,'display_student.html',d1)
        else:
            return HttpResponse('Invalid Data')

    return render(request,'student.html',d)