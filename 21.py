import pandas as pd
from random import randint

class_members = ['Shellawk','Belinda', 'Collins', 'Ericko', 'Faith', 'Calm', 'Gift', 'James', 'Danny', 'Steve', 'Dennis', 'Lawrence']
day_of_the_week = ['mon', 'tue', 'wen', 'thu', 'fri']
dict_days= {
'mon': [],
'tue': [],
'wen': [],
'thu': [],
'fri': []
}

def mark_rigister():
    for i in range(len(class_members)):
        for day in day_of_the_week:
            num = randint(0,1)
            if num == 0:
                dict_days[day].append('O')
            else:
                dict_days[day].append('X')
mark_rigister()

register = pd.DataFrame({
    'Names': class_members,
    'Mon': dict_days['mon'],
    'Tue': dict_days['tue'],
    'Wen': dict_days['wen'],
    'Thu': dict_days['thu'],
    'Fri': dict_days['fri']
})

print('==~CLASS ATTENDANCE REGISTER~==')
print(register)