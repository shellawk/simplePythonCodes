list_of_types_of_fruits = ['citrus', 'stone fruit', 'tropical and exotic', 'berries', 'melons']

dict_fruits = {
    'citrus': ['oranges', 'grapefruits', 'mandarins', 'limes'],
    'stone fruit' : ['nectarines', 'apricots', 'peaches', 'plums'],
    'tropical and exotic': ['bananas', 'mangoes'],
    'berries': ['strawberries', 'raspberries', 'blueberrries', 'kiwifruit', 'passionfruit'],
    'melons': ['watermelons', 'rockmelons', 'honeydew melons']
}

def user_interface():
    for item in list_of_types_of_fruits:
        print(f'{item}: ')
        for i in range(len(dict_fruits[item])):
            print(f'{i+1}. {dict_fruits[item][i]}')
        print('\n')

user_interface()