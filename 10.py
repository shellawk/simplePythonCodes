def user_interface():
    print('Enter the range of odd numbers to be displayed')
    min_num = int(input('Enter the lower limit: '))
    max_num = int(input('Enter the upper limit: '))
    get_odd_numbers(min_num, max_num)

def get_odd_numbers(lower_limit, upper_limit):
    upper_limit += 1
    for i in range(lower_limit, upper_limit):
        if i%2==0:
            print(i)

user_interface()