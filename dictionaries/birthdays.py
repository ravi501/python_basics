def check_birthdays(birth_days):
    while True:
        print('Enter a name (blank to quit):')
        name = input()

        if name == '':
            break

        if name in birth_days:
            print(birth_days[name] + ' is the birthday of ' + name)
        else:
            print('I do not have the birthday information for ' + name)
            print('What is their birth date')
            birth_date = input()
            birth_days[name] = birth_date
            print('Birth date database updated.')


birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
check_birthdays(birthdays)

print(birthdays['ravi'])