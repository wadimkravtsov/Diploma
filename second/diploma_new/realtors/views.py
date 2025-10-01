from django.shortcuts import render
from realtors.models import Realtor


def realtors(request):
    rl = Realtor.objects.all()
    context = {
        "realtors": rl
    }
    return render(request, 'realtors/realtors.html', context)
