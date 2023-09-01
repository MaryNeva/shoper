from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

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


def main_page(request):
    return HttpResponse("Your shop list")


def get_product(request, product):
    description = products_dict.get(product.title(), None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"Page not found")
