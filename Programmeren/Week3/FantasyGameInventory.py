def displayInventory(inventory):
    totalItems = 0
    print ('Inventory:')
    for k, v in inventory.items():
        totalItems += v
        print (v, end=" ")
        print (k)
    
    print ('Total number of items: ' + str(totalItems))
        

playerInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(playerInventory)