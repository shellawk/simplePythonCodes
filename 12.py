import math

def user_interface():
    length = int(input('Enter the length: '))
    radius = int(input('Enter the width: '))
    if length>0 and radius > 0:
        calculate_volume_of_earthworm(length, radius)
    else:
        print('Enter valid dimensions')
        user_interface()

def calculate_volume_of_earthworm(length, radius):
    volume = math.pi * radius * radius * length
    print(f'The volume of the earthworm rounded to 4 decimal places is {volume.__round__(4)} square centimetres')
print('CALCULATE VOLUME OF EARTHWORM IN SQUARE CENTIMETRES')
user_interface()