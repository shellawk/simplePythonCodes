def user_interface():
    name = input('Enter your name: ')
    if len(name) == 0:
        print('Can\'t get name tag without a name')
        print('Please enter a name!!')
        user_interface()
    else:
        create_name_tag(name)

def create_name_tag(user_name):
    name_len = len(user_name)
    line_num = name_len + 8
    print('-' * line_num)
    print(f'|## {user_name} ##|')
    print('-' * line_num)

print('CREATE NAME TAG')
user_interface()