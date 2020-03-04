def user_interface():
    name = input('Enter your name: ')
    if len(name) == 0:
        print('Please enter a name!!')
        user_interface()
    else:
        display_name(name)
        
def display_name(user_name):
    name_len = len(user_name)
    line_num = name_len + 8
    print('*' * line_num)
    print(f'*** {user_name} ***')
    print('*' * line_num)

user_interface()