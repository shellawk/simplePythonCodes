import datetime

current_year = datetime.date.today().year

def user_interface():
    age = int(input('How old are  you: '))
    maximum_human_lifesapn = 160 #according to wikipedia
    if age>=0 and age <= maximum_human_lifesapn:
        get_year_of_birth(current_year, age)
    else:
        print('Invalid input.')
        print('TRY AGAIN!!')
        user_interface()

def get_year_of_birth(current_year, current_age):
    year_born = current_year - current_age
    print(f'You were born between {year_born-1} and {year_born+1}.')
user_interface()