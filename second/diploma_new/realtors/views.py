from django.shortcuts import render, redirect
from realtors.models import Realtor, Cottage
from .forms import CottageForm



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

def create_cottage(request):
    form = CottageForm()

    if request.method == "POST":
        form = CottageForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('realtors')

    context = {'form': form}
    return render(request, 'realtors/form-cottage.html', context)

def update_cottage(request,pk):
    cottage = Cottage.objects.get(id=pk)
    form = CottageForm(instance=cottage)

    if request.method == "POST":
        form = CottageForm(request.POST,instance=cottage)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('realtors')

    context = {'form': form,
               'cottage': cottage}
    return render(request, 'realtors/form-cottage.html', context)

def delete_cottage(request, pk):
    cottage = Cottage.objects.get(id=pk)

    # if request.method == "POST":
    cottage.delete()
    return redirect('realtor', pk=cottage.rlt)

    # context = {'object': cottage}
    # return render(request, 'projects/delete.html', context)


