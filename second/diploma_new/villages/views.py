from django.db.models.expressions import result
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.defaultfilters import title

from .models import Village
from realtors.models import Cottage


def villages(request):
    search_village = ""
    if request.GET.get('search_village'):
        search_village = request.GET.get('search_village')

    vg = Village.objects.filter(title__icontains=search_village)

    page = request.GET.get('page')
    result = 3
    paginator = Paginator(vg, result)

    try:
        vg = paginator.page(page)  # http://127.0.0.1:8000/projects/?page=2
    except PageNotAnInteger:
        page = 1
        vg = paginator.page(page)  # http://127.0.0.1:8000/projects/?page=fgdfgdfg
    except EmptyPage:
        page = paginator.num_pages
        vg = paginator.page(page)

    context = {
        "villages": vg,
        "search_village": search_village,
        "paginator": paginator
    }
    return render(request, 'villages/villages.html', context)

def village(request, pk):
    village.obj = Village.objects.get(id=pk)
    cottages = Cottage.objects.filter(village=village.obj.title)
    print(cottages)
    return render(request, 'villages/one_village.html', {'village': village.obj, 'cottages': cottages})
