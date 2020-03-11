import sys

birthdays = {'jasmine': 'july 11, 2019',
             'david': 'september 9, 1998',
             'james': 'december 4, 2015'}
possible_answers = ['add', 'delete', 'get']


questionnaire = input('Do you want to add/delete/get celebrant?')
if questionnaire == 'get':
    def birth_getter(name):
        if name in birthdays:
            print(name + "'s birthday is " + birthdays.get(name))
        else:
            print(name + "'s birthday is not in the DB")
            sys.exit('Exiting machine>>>')
        return name

    birth_getter(input('Enter celebrant name: '))
if questionnaire not in possible_answers:
    sys.exit('Invalid input...Exiting machine>>>')


if questionnaire == 'add':
    initial_count = 0
    how_many_add = input('How many are you adding to the DB?')
    while initial_count < int(how_many_add):
        initial_count += 1
        new_celebrant = input('Enter celebrant name: ')
        if new_celebrant in birthdays:
            print('Celebrant already in DB!')
            sys.exit('Exiting machine>>>')
        else:
            new_celebrant_date = input('Enter birthday: ')
            print('*' * 20)
            birthdays[new_celebrant] = new_celebrant_date
elif questionnaire == 'delete':
    del_celebrant = input('Enter celebrant name: ')
    if del_celebrant not in birthdays:
        print('celebrant not in DB!')
        sys.exit('Exiting machine>>>')
    else:
        del birthdays[del_celebrant]


if questionnaire == 'add' and int(how_many_add) > 1:
    print('The celebrants have been added to the DB!')
elif questionnaire == 'get':
    print('*' * 20)
elif questionnaire == 'delete':
    print(del_celebrant + "'s data has been removed from the DB")
elif questionnaire == 'add' and int(how_many_add) == 1:
    print('The celebrant has been added to the DB!')
