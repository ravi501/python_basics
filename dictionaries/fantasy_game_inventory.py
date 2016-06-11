
def display_inventory(stuff):
    print('Inventory:')
    item_total = 0
    for key,value in stuff.items():
        print(str(value) + ' ' + str(key))
        item_total += value
    print('Total number of items ' + str(item_total))

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(inventory)