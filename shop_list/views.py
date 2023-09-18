from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import Product, Catalog_section
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

products_dict = {
    'Grocery': [
        'chips', 'dried', 'fruit', 'eggs', 'flour', 'ketchup', 'margarine', 'mayonnaise', 'mustard', 'nuts', 'olive',
        'oil', 'olives', 'pistachios', 'prunes', 'raisins', 'seeds', 'soy', 'sauce', 'starch', 'tomato', 'paste',
        'vegetable', 'oil', 'vinegar', 'yeast'],
    'Greens': [
        'basil', 'cilantro', 'dill', 'green', 'onion', 'parsley', 'salad'],
    'Confectionery': [
        'cake', 'cakes', 'candies', 'cooking', 'chocolate'],
    'Coffee, tea': [
        'black', 'tea', 'green', 'tea', 'coffee', 'beans', 'ground', 'coffee', 'instant', 'coffee'],
    'Pasta': [
        'lasagna(sheets)', 'pasta', 'spaghetti', 'vermicelli'],
    'Dairy': [
        'baked milk', 'butter', 'cheese', 'cheeses', 'condensed', 'milk', 'cream', 'curds', 'ice', 'cream', 'kefir',
        'milk', 'sour', 'cream', 'yogurt'],
    'Seafood': [
        'crab', 'sticks', 'crabs', 'fresh', 'fish', 'frozen', 'fish', 'herring', 'Mackerel', 'mussels', 'red', 'caviar',
        'rolls', 'shrimp', 'sprats', 'sushi', 'caviar', 'black'],
    'Meat': [
        'products', 'beef', 'chicken', 'meat', 'lard', 'pate', 'pelmeni', 'pork', 'rabbit', 'sausage', 'sausages',
        'turkey'],
    'Drinks': [
        'coca - cola', 'juice', 'kvass', 'lemonade', 'Mineral', 'water'],
    'Vegetables': [
        'beans', 'beet', 'cabbage', 'carrot', 'cauliflower', 'celery', 'corn', 'cucumber', 'eggplant', 'eggplant',
        'caviar', 'Garlic', 'ginger', 'mushrooms', 'horseradish', 'onion', 'peas', 'pepper', 'pickled', 'ginger',
        'potatoes', 'pumpkin', 'radish', 'tomatoes', 'zucchini'],
    'Fruits': [
        'apple', 'pineapple', 'apricots', 'avocado', 'bananas', 'berries', 'cherries', 'grapes', 'melon', 'nectarines',
        'pears', 'plums', 'persimmon', 'raspberries', 'strawberries', 'watermelon'],
    'Spice': [
        'salt', 'red', 'pepper', 'black', 'pepper', 'bay', 'leaf'],
}


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
