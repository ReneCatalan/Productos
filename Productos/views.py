from django.shortcuts import render
from Productos.models import *
from Productos.forms import *
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login




#Views Cars
@login_required(login_url='/auth/login')
def list(request):
    
    data= {}
    
    data["request"] = request
    object_list = Producto.objects.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)
    template_name = 'list.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def add(request):
    
    data = {}
    data["request"] = request
    if request.method == "POST":
        data['form'] = ProductoForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('list')

    else:
        data['form'] = ProductoForm()

    template_name = 'add.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def delete(request, id):
    
    data = {}
    template_name = 'list.html'
    data['Producto'] = Producto.objects.all()
    Producto.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse('list'))

@login_required(login_url='/auth/login')
def edit(request, car_id):
    
    data = {}
    data['tittle'] = "Editar"
    data["request"] = request
    if request.POST:
        formP = EditProducto(request.POST, request.FILES, instance=Producto.objects.get(pk=id))
        if formP.is_valid():
            formP.save()
            return redirect('list')
    template_name = 'edit.html'
    data['data'] = EditProducto(instance=Producto.objects.get(pk=id))

    return render(request, template_name, data)

