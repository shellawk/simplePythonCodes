import calendar

def user_interface():
    year = int(input('Enter the year: '))
    month = int(input('Enter the month: '))
    if year>0 and month < 12 and month > 0:
        print(calendar.month(year, month))
    else:
        print('Invalid input!! TRY AGAIN.')

user_interface()
