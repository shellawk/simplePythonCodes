def user_interface():
    first_num = int(input('Enter the first number: '))
    second_num = int(input('Enter second number: '))
    operator_choice = select_operator()
    calculator(first_num, second_num, operator_choice)

def select_operator():
    list_of_operators = ['add', 'subtract', 'multiply', 'devide']
    for i in range(4):
        print(f'{i+1}. {list_of_operators[i]}')
    operator = int(input('Select operation: '))
    if operator >= 1 and operator<= 4:
        return operator
    else:
        print('Invalid Choice!!')
        user_interface()

def calculator(num1, num2, the_operator):
    if the_operator == 1:
        print(f'{num1} + {num2} = {num1+num2}')
    elif the_operator == 2:
        print(f'{num1} - {num2} = {num1-num2}')
    elif the_operator == 3:
        print(f'{num1} * {num2} = {num1*num2}')
    else:
        print(f'{num1} / {num2} = {num1/num2}')

print('++~SIMPLE CALCULATOR~++')
user_interface()