from django.shortcuts import render
from .models import Village

def villages(request):
    vg = Village.objects.all()
    context = {
        "villages": vg
    }
    return render(request, 'villages/villages.html', context)
