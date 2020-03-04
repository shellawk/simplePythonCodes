import os

male_clothes = ['top hat', 'trouser', 'shirts', 't-shirts']
female__clothes = ['skirts', 'dress', 'bra']
gender = ['Male', 'Female']

def get_male_clothes():
    for item in male_clothes:
        print(item)

def get_female_clothes():
    for item in female__clothes:
        print(item)

def user_interface():
    for i in range(2):
        print(f'{i+1}. {gender[i]}')
    choice_of_gender = int(input('Chose gender from above: '))
    
    if choice_of_gender >= 1 and choice_of_gender <= 2:
        if choice_of_gender == 1:
            get_male_clothes()
        else:
            get_female_clothes()
    else:
        os.system('cls')
        print('Invalid Choice!! Try Again!')
        user_interface()

user_interface()