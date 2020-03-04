list_of_cars = ['mercedes', 'harrier', 'range rover', 'rolls royce', 'bugatti', 'ferrari']

class FavoriteCar:
    def __init__(self, name):
        self.name = name
        
    price_of_cars = {
        'mercedes': 30000000,
        'harrier': 3200000,
        'range rover': 8000000,
        'bugatti': 1100000000,
        'ferrari': 500000000,
        'rolls royce' : 900000000
    }


def user_interface():
    get_list_of_car()
    car_num = int(input('Select your favourite car: '))
    if car_num >= 1 and car_num <= len(list_of_cars):
        car = FavoriteCar(list_of_cars[car_num-1])
        print(f'The price of {car.name} is {car.price_of_cars[car.name]}')
    else:
        print('Invalid choice!! TRY AGAIN.')
        user_interface()

def get_list_of_car():
    for i in range(len(list_of_cars)):
        print(f'{i+1}. {list_of_cars[i]}')

print('GET THE PRICE OF YOUR FAVOURITE CAR')
user_interface()