from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import Product, Catalog_section
from .forms import Login, Product_form
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



def show_product(request, slug_product:str, slug_section: str):
    name = get_object_or_404(Product, slug=slug_product)
    objects = Product.objects.filter(name=name)
    return render(request, 'shop_list/product.html', context={'objects': objects})


def get_login(request):
    if request.method == 'POST':
        login = Login(request.POST)
        return render(request, 'shop_list/log_in.html', context={'login': login})
    login = Login()
    return render(request, 'shop_list/log_in.html', context={'login': login})


def get_product(request):
    if request.method == 'GET':
        product_form = Product_form(request.GET)
        return render(request, 'shop_list/section.html', context={'product_form': product_form})
    product_form = Product_form()
    return render(request, 'shop_list/section.html', context={'product_form': product_form})