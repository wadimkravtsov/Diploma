from django.shortcuts import render
from .models import Village

def villages(request):
    vg = Village.objects.all()
    context = {
        "villages": vg
    }
    return render(request, 'villages/villages.html', context)

def village(request, pk):
    village.obj = Village.objects.get(id=pk)
    return render(request, 'villages/one_village.html', {'village': village.obj})
