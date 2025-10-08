from django.shortcuts import render
from realtors.models import Realtor, Cottage



def realtors(request):
    rl = Realtor.objects.all()
    context = {
        "realtors": rl
    }
    return render(request, 'realtors/realtors.html', context)

def realtor(request, pk):
    realtor.obj = Realtor.objects.get(id=pk)
    cottages = Cottage.objects.filter(rlt=pk)
    context = {
        'realtor': realtor.obj,
        'cottages': cottages
    }
    print(cottages, pk)
    return render(request, 'realtors/one_realtor.html', context)

