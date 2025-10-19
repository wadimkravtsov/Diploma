from django.shortcuts import render
from .models import Village
from realtors.models import Cottage


def villages(request):
    vg = Village.objects.all()
    context = {
        "villages": vg
    }
    return render(request, 'villages/villages.html', context)

def village(request, pk):
    village.obj = Village.objects.get(id=pk)
    cottages = Cottage.objects.filter(village=village.obj.title)
    print(cottages)
    return render(request, 'villages/one_village.html', {'village': village.obj, 'cottages': cottages})
