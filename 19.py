def user_interface():
    student_marks = int(input('Enter your marks: '))
    if student_marks > 0 and student_marks < 100:
        add_to_record(str(student_marks))
        display_student_marks(student_marks)
    else:
        print('Enter valid marks!!')

def display_student_marks(marks):
    print('Your marks has been store successfully!!')
    choice = input('Enter Y to display your record else enter N to exit this program: ').lower()
    if choice == 'y':
        get_record()
    else:
        pass

def add_to_record(marks_to_add):
    with open('records.txt', 'a') as f:
        f.write(marks_to_add + '\n')
def get_record():
    print('Here are your record(s): ')
    with open('records.txt', 'r') as f:
        print(f.read())

user_interface()