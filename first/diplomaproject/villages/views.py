from django.shortcuts import render

def villages(request):
    return render(request, 'villages/villages.html')
