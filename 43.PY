actual_name = 'Shellawk'.lower() #change this name to yours

def user_interface():
    name = input('Enter your name: ').lower()
    if len(name) == 0:
        print('Please enter a name!!')
        user_interface()
    else:
        check_name(name)

def check_name(user_name):
    if actual_name == user_name:
        print('Correct spelling')
    else:
        print('Wrong Spelling!!')
        print('TRY AGAIN!!')
        user_interface()

user_interface()