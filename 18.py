def user_interface():
    mass = int(input('Enter your mass in kg: '))
    height = int(input('Enter your height in cm: '))
    if mass > 0 and height > 0:
        bmi = calculate_bmi(mass, height)
        print(bmi)
        interprete_bmi(bmi)
    else:
        print('Invalid input. TRY AGAIN!!')
        user_interface()

def calculate_bmi(body_mass, body_height):
    body_height_in_m = body_height/100
    body_height_squared = body_height_in_m ** 2
    print(body_height_squared)
    bmi = body_mass/body_height_squared
    return bmi

def interprete_bmi(bmi):
    if bmi < 18.5:
        print('Below Normal Weight.')
    elif bmi >= 18.5 and bmi < 25:
        print('Normal Weight.')
    elif bmi >= 25 and bmi < 30:
        print('Overweight.')
    elif bmi>=30 and bmi < 35:
        print('Class I Obesity.')
    elif bmi >= 35 and bmi < 40:
        print('Class II Obesity.')
    else:
        print('Class III Obesity.')

user_interface()