import random

def get_random_numbers(list_of_parameters):
    list_of_random_numbers = []
    for i in range(list_of_parameters[2]):
        list_of_random_numbers.append(random.randint(list_of_parameters[0], list_of_parameters[1]))
        print(list_of_random_numbers[i])

#prompt the user to enter the range
def user_interface():
    min_num = int(input('Enter the lower limit: '))
    max_num = int(input('Enter the upper limit: '))
    num_range = int(input('How man numbers should be genarated: '))
    return [min_num, max_num, num_range]

def run_prog():
    list_of_arguments = user_interface()
    get_random_numbers(list_of_arguments)

try:
    run_prog()

except ValueError as e:
    print('Invalid entry!! TRY AGAIN!!')

