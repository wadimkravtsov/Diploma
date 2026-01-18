from django.shortcuts import render, redirect
from realtors.models import Realtor, Cottage
from django.contrib.auth.models import User
from .forms import CottageForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def realtors(request):
    search_realtor = ""
    if request.GET.get('search_realtor'):
        search_realtor = request.GET.get('search_realtor')

    rl = Realtor.objects.filter(title__icontains=search_realtor)

    page = request.GET.get('page')
    result = 3
    paginator = Paginator(rl, result)

    try:
        rl = paginator.page(page)  # http://127.0.0.1:8000/projects/?page=2
    except PageNotAnInteger:
        page = 1
        rl = paginator.page(page)  # http://127.0.0.1:8000/projects/?page=fgdfgdfg
    except EmptyPage:
        page = paginator.num_pages
        rl = paginator.page(page)

    left_number = int(page) - 2
    if left_number < 1:
        left_number = 1

    right_number = int(page) + 3
    if right_number > paginator.num_pages:
        right_number = paginator.num_pages + 1

    pages_range = range(left_number, right_number)

    context = {
        "realtors": rl,
        "search_realtor": search_realtor,
        "paginator": paginator,
        "pages_range": pages_range
    }
    return render(request, 'realtors/realtors.html', context)

def realtor(request, pk):
    realtor.obj = Realtor.objects.get(id=pk)
    cottages = Cottage.objects.filter(rlt=pk)
    if request.user.is_authenticated:
        numb = request.user.profile.realt.id
    else:
        numb = 0
    print(numb)
    print(pk)

    context = {
        'realtor': realtor.obj,
        'cottages': cottages,
        'numb': int(numb),
        'pk': int(pk)
    }
    print(cottages, pk)
    return render(request, 'realtors/one_realtor.html', context)

def create_cottage(request):
    form = CottageForm()

    if request.method == "POST":
        form = CottageForm(request.POST)
        rt = request.POST['rlt']
        # print(form.fields)
        # print(rt)
        if form.is_valid():
            form.save()
            return redirect('realtor', pk=rt)

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


