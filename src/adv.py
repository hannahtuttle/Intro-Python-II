from room import Room
from player import Player
from item import Item

# declare all items

items = {
    "coin": Item('coin', "a small gold coin, it looks pretty old"),
    "pen": Item('pen', "this pen looks new, maybe i should fins some paper to test it."),
    "sword": Item('sword', 'a rusty old sword stuck inside a rock.'),
    "chest": Item('chest', "a small old chest, it's locked"),
    "key": Item('key', "an old key, I wonder what this could be for?"),
    "book": Item('book', 'it looks like there are a few pages missing.'),
    "candle": Item('candle', 'you brought this with you because you might end up in a dark room')
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items["key"].name]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items["pen"].name]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items["sword"].name, items["coin"].name, items["chest"].name]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items["book"].name]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
# print(room['outside'].name)

# Make a new player object that is currently in the 'outside' room.
player_1 = Player('player_1',room['outside'])

# print(f'players current room: {player_1.current_room}')
# print(f'description for current room: {room["outside"].description}')


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def check_items(item_array):
    if len(item_array) == 0:
        print(f'You look around but you do not find anything')
    elif len(item_array) >= 1:
        print(f'You look around the room and see a...')
        for x in item_array:
            print(f'{x}')


def check_command(command):
    if len(command) == 0:
        pass
    elif len(command) == 1:
        pass
    elif command[0] == 'take' or command[0] == 'get':
        print(command)
        print('drop stopping here?????')
        player_1.on_take(command)
    elif command[0] == 'drop':
        print("checking to see if drop gets here!!")
        player_1.on_drop(command)
        print("checking to see if drop gets here after calling the drop function!!")
    else:
         print('Not a valid command.')


while True:
    print(f'{player_1.current_room.name}')
    print(f'{player_1.current_room.description}')
    check_items(player_1.current_room.items)
    
    # item_input_choice = input("take/drop item from/in the room (must be only one space between command and item): ").split(' ')
    
    player_input = input("--> ").split(' ')
    check_command(player_input)
    # print(f'command: {item_input_choice[0]} and item: {item_input_choice[1]}')

    if player_input[0] == 'n':
        if player_1.current_room.n_to is None:
            print("you cannot go that way")
        else:
            player_1.current_room = player_1.current_room.n_to
    elif player_input[0] == 's':
        if player_1.current_room.s_to is None:
            print("you cannot go that way")
        else:
            player_1.current_room = player_1.current_room.s_to
    elif player_input[0] == 'e':
        if player_1.current_room.e_to is None:
            print("you cannot go that way")
        else:
            player_1.current_room = player_1.current_room.e_to
    elif player_input[0] == 'w':
        if player_1.current_room.w_to is None:
            print("you cannot go that way")
        else:
            player_1.current_room = player_1.current_room.w_to
    elif player_input[0] == 'i' or player_input[0] == 'inventory':
        print("items in your inventory: ")
        if len(player_1.items) == 0:
            print('You have no items in your inventory')
        else:
            for it in player_1.items:
                print(f'{it}')
    elif player_input[0] == 'q':
        print('See you next time!')
        break