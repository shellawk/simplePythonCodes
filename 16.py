relationship_to_family_member = ['father', 'mother', 'sister', 'brother', 'aunt', 'uncle']

family_members = {
    'father': 'Osman',
    'mother': 'Ambiya',
    'sister': 'Fatuma',
    'brother': 'Omar',
    'uncle': 'Mohamed',
    'aunt': 'Noor'
    }

def user_interface():
    get_type_of_relationship()
    family_member = int(input('Select the kind of relationship: '))
    if family_member >= 0 and family_member <= len(relationship_to_family_member):
        get_name(family_member-1)
    else:
        print('Invalid Choice!!. TRY AGAIN.')
        user_interface()

def get_type_of_relationship():
    for i in range(len(relationship_to_family_member)):
        print(f'{i+1}. {relationship_to_family_member[i]}')

def get_name(num):
    print(f'Your {relationship_to_family_member[num]}\'s name is {family_members[relationship_to_family_member[num]]}')

user_interface()