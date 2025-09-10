from django.shortcuts import render

def realtors(request):
    return render(request, 'realtors/realtors.html')
