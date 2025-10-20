from django.shortcuts import render
from django.template.defaultfilters import title

from .models import Village
from realtors.models import Cottage


def villages(request):
    search_village = ""
    if request.GET.get('search_village'):
        search_village = request.GET.get('search_village')

    vg = Village.objects.filter(title__icontains=search_village)
    context = {
        "villages": vg,
        "search_village": search_village
    }
    return render(request, 'villages/villages.html', context)

def village(request, pk):
    village.obj = Village.objects.get(id=pk)
    cottages = Cottage.objects.filter(village=village.obj.title)
    print(cottages)
    return render(request, 'villages/one_village.html', {'village': village.obj, 'cottages': cottages})
