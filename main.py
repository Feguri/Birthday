import random

people_dict = {}

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']

days_31 = ['1', '2', '3', '4', ' 5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

days_30 = ['1', '2', '3', '4', ' 5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']

days_29 = ['1', '2', '3', '4', ' 5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29']


def random_birthday(num_of_people):
    for num in range(0, num_of_people):
        month = random.choice(months)

        if month == 'February':
            day = random.choice(days_29)

        elif month == 'April' or month == 'June' or month == 'September' or month == 'November':
            day = random.choice(days_30)

        else:
            day = random.choice(days_31)

        people_dict[f'person {num + 1}'] = [f'{month}', f'{day}']

        print(f'person {num + 1} birthday is {month} {day}.')


def birthday_check():
    current_person = 1
    second_current_person = 1
    match = False
    num_of_matches = 0
    for person in people_dict:
        for second_person in people_dict:
            key_list = list(people_dict.keys())

            person_key = key_list[current_person - 1]
            second_person_key = key_list[second_current_person - 1]
            birthday = people_dict[f'person {current_person}']
            
#            If statement that looks for matches. 
            if people_dict[f'person {current_person}']\
                    == people_dict[f'person {second_current_person}'] and person_key != second_person_key\
                    and people_dict[f'person {current_person}'] is not None:

                print(f'\nThere is a match! {person_key} and {second_person_key} both have their birthdays on '
                      f'{birthday[0]} {birthday[1]}.')
          
#               Cancels current persons birthdays so it does not detect corss matches. Example: person 1 & person 2 and person 2 & person 1
#               However, it might prevent multiple birthday matches in a large room. (problem in detail at Readme.md)
                people_dict[f'person {current_person}'] = None
                people_dict[f'person {second_current_person}'] = None
                match = True
                num_of_matches += 1

            second_current_person += 1

        current_person += 1
        second_current_person = 1
    if not match:
        print('\nThere are no birthday matches.')
    else:
        print(f'\nThe number of matches in this room was {num_of_matches}.')


def calculate_probability(num_of_people):

    pairs = (num_of_people * (num_of_people - 1)) / 2

    probability = round(((364/365) ** pairs) * 100, 2)
    result = 100 - probability

    print(f'\nThe probability of at least one match in a room with {num_of_people} people was {round(result, 3)}%')

# Play with this number and experiment with different results
people = 40

random_birthday(num_of_people=people)
birthday_check()
calculate_probability(num_of_people=people)
