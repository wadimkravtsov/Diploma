from django.shortcuts import render, redirect
from realtors.models import Realtor, Cottage
from .forms import CottageForm



def realtors(request):
    search_realtor = ""
    if request.GET.get('search_realtor'):
        search_realtor = request.GET.get('search_realtor')

    rl = Realtor.objects.filter(title__icontains=search_realtor)
    context = {
        "realtors": rl,
        "search_realtor": search_realtor
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
        print(form.fields)
        if form.is_valid():
            form.save()
            return redirect('realtors', pk=form.rlt.id)

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
            return redirect('realtor', pk=cottage.rlt.id)

    context = {'form': form,
               'cottage': cottage}
    return render(request, 'realtors/form-cottage.html', context)

def delete_cottage(request, pk):
    cottage = Cottage.objects.get(id=pk)

    # if request.method == "POST":
    cottage.delete()
    return redirect('realtor', pk=cottage.rlt.id)

    # context = {'object': cottage}
    # return render(request, 'realtors/form-cottage.html', context)


