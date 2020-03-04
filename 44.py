def user_interface():
    name = input('Enter your name: ')
    if len(name) == 0:
        print('Please enter a name!!')
        user_interface()
    else:
        index_name(name)

def index_name(user_name):
    list_of_char = []
    for character in user_name:
        list_of_char.append(character)
    for i in range(len(list_of_char)):
        print(f'{i}. {list_of_char[i]}')

print('INDEX THE SPELLING OF YOUR NAME')
user_interface()