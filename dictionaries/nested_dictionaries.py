

def total_brought(all_guests, item):
    num_brought = 0
    for k,v in all_guests.items():
        num_brought = num_brought + v.get(item, 0)
    return num_brought



all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

print('Number of things being brought')
print('  - Apples ' +  str(total_brought(all_guests, 'apples')))
print('  - Pretzels ' +  str(total_brought(all_guests, 'pretzels')))
print('  - ham sandwiches ' +  str(total_brought(all_guests, 'ham sandwiches')))
print('  - cups ' +  str(total_brought(all_guests, 'cups')))
print('  - apple pies ' +  str(total_brought(all_guests, 'apple pies')))
