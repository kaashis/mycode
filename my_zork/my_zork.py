#!/usr/bin/python3
import os
clear = lambda: os.system('clear')

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
    go [direction]  - move to a specified direction
    get [item]      - get the item you see
    open [door]     - open the door you see
    teleport        - teleport to a room/place
    quit            - quit the game
''')


def showStatus():  
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ',inventory)
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ',list(rooms[currentRoom]["item"].keys()))
    print("---------------------------")

    #print(rooms[currentRoom]["item"])

    # for each place, show the directions and places you can go to 
    if 'east' in rooms[currentRoom]:
        print(f"You can go east to {rooms[currentRoom]['east']}")
    if 'west' in rooms[currentRoom]:
        print(f"You can go west to {rooms[currentRoom]['west']}")
    if 'north' in rooms[currentRoom]:
        print(f"You can go north to {rooms[currentRoom]['north']}")
    if 'south' in rooms[currentRoom]:
        print(f"You can go south to {rooms[currentRoom]['south']}")

def teleport():
    print("Where would you like to teleport? or press 'q' to cancel!\n")
    print(list(rooms.keys()))
    destination = input(">").lower()
    if(destination=='q'):
        clear()
    elif destination in [room.lower() for room in list(rooms.keys())]:
        if destination=='bedroom' and 'key' not in inventory:
            print("You need a KEY to teleport to the Bedroom!")
            teleport()
        else:
            global currentRoom
            currentRoom= destination.title()
    else:
        print("Please enter a valid room from the list or q to cancel")
        teleport()

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'west': 'Bedroom',
        'item': {
            'key':'You can open bedroom with this key',
            'torch': 'You can use torch in dark rooms'
            }
    },

    'Kitchen': {
        'north': 'Hall',
        'item': {
            'monster':'This monster will eat you if you go bare handed'
            },
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': {
            'potion':'The potion will heal you',
            'door':'You can open the door to go through it',
            'meat':'Animals like tiger would like a loaf of meat'
            },
        'north': 'Pantry',
    },
    'Garden': {
        'north': 'Dining Room',
        'east' : 'Forest',
        'item':{
            'horse': 'You can ride the horse',
            'fruits':'You can eat the fruits'
            }
    },
    'Pantry': {
        'south': 'Dining Room',
        'item': {
            'cookie': 'You can eat the cookie when you are hungry'
            },
    },
    'Bedroom':{
        'east':'Hall',
        'item':{
            'sword': 'You can use the sword to kill the tiger'
            }
    },
    'Forest':{
        'west':'Garden',
        'item':{
            'tiger': 'You can kill the tiger with the sword if you have it, otherwise tiger eats you'
            }
    }
}

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# loop forever
while True:
    showStatus()
    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)
    
    #clear the screen
    clear() 
    #if they type 'quit:'
    if move[0] == 'quit':
        break

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            if rooms[currentRoom][move[1]]=='Bedroom' and 'key' not in inventory:
                print("Oh no... The door is locked. Please get the key for the bedroom first!")
            else:
                # set the current room to the new room
                currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            if move[1]=='door':
                print("You can not get door. Please use: open door")
            else:
                # add the item to their inventory
                inventory += [move[1]]
                # display a helpful message
                print(move[1] + ' got!')
                print(rooms[currentRoom]['item'][move[1]])

                #delete an item from the dictionary "item"
                del rooms[currentRoom]['item'][move[1]]

                # delete the item from the room if the dictionary item has no values
                if (len(rooms[currentRoom]['item'])<1):
                    del rooms[currentRoom]['item']

        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
        
    if move[0] == 'open' and move[1] in rooms[currentRoom]['item'] and move[1]=='door':
        print("This was a trapdoor. You are now trapped....Game Over!")
        break
    if move[0] == 'teleport':
        teleport()

    ## Define how a player can win and or lose
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
    elif currentRoom == 'Forest':
        if 'sword' in inventory and 'meat' in inventory and 'item' in rooms[currentRoom]:
            def prompts():
                print("Please select a or b:")
                print("a. Kill the tiger with your sword")
                print("b. Offer tiger the loaf of meat")

            prompts()
            selection = input(">")
            if selection == 'a':
                del rooms[currentRoom]['item']
                print("You killed the tiger and saved your life. Good job!")
            elif selection =='b':
                inventory.remove('meat')
                print("Hooray..You befriended the tiger. He showed you way out of the forest and you escaped. You Win!!")
                break
            else:
                print("Invalid selection! Please select a  or b")
                prompts()
        elif 'sword' in inventory and 'item' in rooms[currentRoom]:
            del rooms[currentRoom]['item']
            print("You killed the tiger and saved your life. Good job!")
        elif 'meat' in inventory and 'item' in rooms[currentRoom]:
            inventory.remove('meat')
            print("The tiger ate the meat and let you live...Lucky Day for you!")
        elif 'item' in rooms[currentRoom]:
            print('A tiger has got you... GAME OVER!')
            break
        else:
            continue

    ## If a player enters a room with a monster
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        #If the player has the cookie
        if 'cookie' in inventory:
            print('A monster has snatched your cookie and ran away!')
        
            #delete monster from that room and cookie from the inventory
            del rooms[currentRoom]['item']["monster"]
            inventory.remove('cookie')

            # delete the item from the room if the dictionary item has no values
            if (len(rooms[currentRoom]['item'])<1):
                del rooms[currentRoom]['item']
            continue
        else:
            print('A monster has got you... GAME OVER!')
            break

