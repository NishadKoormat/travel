from django.shortcuts import render
from . models import Place,Team

# Create your views here.
def display(request):
    obj1=Place.objects.all()
    obj2=Team.objects.all()
    return render(request,'index.html', {'places':obj1,'teams':obj2})
