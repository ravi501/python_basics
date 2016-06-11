def display_inventory(stuff):
    print('Inventory:')
    item_total = 0
    for key,value in stuff.items():
        print(str(value) + ' ' + str(key))
        item_total += value
    print('Total number of items ' + str(item_total))

def add_to_inventory(inventory, add_items):
    for item in add_items:
        inventory.setdefault(item, 0)
        count = inventory.get(item)
        count += 1
        inventory[item] = count
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)