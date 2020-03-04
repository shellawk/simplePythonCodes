import pandas as pd
#categories of items available
categories = ['groceries', 'furniture', 'electronics', 'utensils'] 

groceries = ['tomato', 'apple', 'orange', 'avocado', 'passion', 'cabbage']
electronics = ['Television', 'fridge', 'woofer', 'microwave', 'vaccum cleaner', 'toaster']
furniture = ['sofa', 'stool', 'table', 'cupboard']
utensils = ['cup', 'spoon', 'frying pan']

#price of items
groceries_price_per_kg = {
    'tomato': 200,
    'apple': 500,
    'orange': 300,
    'avocado': 450,
    'cabbage': 100,
    'passion': 200
}

electronics_price_per_item = {
    'Television': 20000,
    'fridge': 35000,
    'woofer': 15000,
    'microwave': 32000,
    'vaccum cleaner': 12000,
    'toaster': 2000
}

furniture_price_per_set = {
    'sofa': 40000,
    'stool': 3000,
    'table': 5000,
    'cupboard': 11500
}
utensils_price_per_set = {
    'cup': 500,
    'spoon': 200,
    'frying pan': 650
}

def get_categories():
    print('++Please choose from the following Categories++')
    for i in range(len(categories)):
        print(f'{i+1}. {categories[i]}')

def get_items_in_a_cartegory(category):
    for i in range(len(category)):
        print(f'{i+1}. {category[i]}')

def get_groceries_price_per_kg():
    print('Price of groceries per kg')
    for item in groceries:
        print(f'{item}\t {groceries_price_per_kg[item]}')

def get_furniture_price_per_set():
    print('Price of groceries per kg')
    for item in furniture:
        print(f'{item}\t{furniture_price_per_set[item]}')

def get_utensils_price_per_set():
    print('Price of groceries per kg')
    for item in utensils:
        print(f'{item}\t{utensils_price_per_set[item]}')

def get_electronics_price_per_item():
    print('Price of groceries per kg')
    for item in electronics:
        print(f'{item}\t{electronics_price_per_item[item]}')
    
def get_price(num):
    if num==1:
        get_groceries_price_per_kg()
    elif num==2:
        get_furniture_price_per_set()
    elif num==3:
        get_electronics_price_per_item()
    elif num==4:
        get_utensils_price_per_set()
    else:
        print('Invalid choice!! TRY AGAIN')
        user_interface()

def user_interface():
    get_categories()
    choice_of_cartegory = int(input('Enter the category\'s number: '))
    get_price(choice_of_cartegory)

print('~WELCOME TO SHELLAWK MALL~')
user_interface()