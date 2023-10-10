from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import Product, Catalog_section, Login
from .forms import Login_form, Product_form
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

def show_catalog(request):
    sections = Catalog_section.objects.order_by('name_section')
    return render(request, 'shop_list/catalog.html', context={'sections': sections})

def show_section(request, slug_section: str):
    section = get_object_or_404(Catalog_section, slug=slug_section)
    products = Product.objects.filter(section=section)
    return render(request, 'shop_list/section.html', context={'products': products, 'section': section})






def get_login(request):
    if request.method == 'POST':
        login = Login_form(request.POST)
        if login.is_valid():
            print(login.cleaned_data)
            form_login = Login(
                name=login.cleaned_data['name'],
                surname=login.cleaned_data['surname'],
                nickname=login.cleaned_data['nickname'],
                email=login.cleaned_data['email'],
                password=login.cleaned_data['password'],
            )
            form_login.save()
            return HttpResponseRedirect('/')
            #return render(request, 'shop_list/log_in.html', context={'login': login})
    else:
        login = Login_form()
    return render(request, 'shop_list/log_in.html', context={'login': login})


def info_product(request, slug_product:str, slug_section: str):
    name = get_object_or_404(Product, slug=slug_product)
    objects = Product.objects.filter(name=name)
    if request.method == 'POST':
        product_form = Product_form(request.POST)
        if product_form.is_valid():

            form = Product(
                name=product_form.cleaned_data['name'],
                name_unit=product_form.cleaned_data['name_unit'],
                counting=product_form.cleaned_data['counting'],
                comment=product_form.cleaned_data['comment'],
            )
            form.save()
            return render(request, 'shop_list/product.html', context={'product_form': product_form, 'objects': objects})
    else:
        product_form = Product_form()
    return render(request, 'shop_list/product.html', context={'product_form': product_form, 'objects': objects})


#def show_product(request, slug_product:str, slug_section: str):
#    name = get_object_or_404(Product, slug=slug_product)
#    objects = Product.objects.filter(name=name)
#    return render(request, 'shop_list/product.html', context={'objects': objects})