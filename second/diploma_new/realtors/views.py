from django.shortcuts import render
from realtors.models import Realtor


def realtors(request):
    rl = Realtor.objects.all()
    context = {
        "realtors": rl
    }
    return render(request, 'realtors/realtors.html', context)

def realtor(request, pk):
    realtor.obj = Realtor.objects.get(id=pk)
    return render(request, 'realtors/one_realtor.html', {'realtor': realtor.obj})

