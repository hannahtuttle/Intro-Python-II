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
player_1 = Player('player_1',room['outside'].name, [items["candle"].name])

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

# direction_choices = ['n', 's', 'e', 'w']
def check_items(item_array):
    if len(item_array) == 0:
        print(f'You look around but you do not find anything')
    elif len(item_array) >= 1:
        print(f'You look around the room and see a...')
        for x in item_array:
            print(f'{x}')

while True:
    print(f'{player_1.current_room}')

    if player_1.current_room == room["outside"].name:
        print(f'{room["outside"].description}')
        check_items(room["outside"].items)
    elif player_1.current_room == room["foyer"].name:
        print(f'{room["foyer"].description}')
        check_items(room["foyer"].items)
    elif player_1.current_room == room["overlook"].name:
        print(f'{room["overlook"].description}')
        check_items(room["overlook"].items)
    elif player_1.current_room == room["narrow"].name:
        print(f'{room["narrow"].description}')
        check_items(room["narrow"].items)
    elif player_1.current_room == room["treasure"].name:
        print(f'{room["treasure"].description}')
        check_items(room["treasure"].items)
    
    player_input = input("chose your direction wisely: ")

    if player_input == 'n':
        if player_1.current_room == room["outside"].name:
            player_1.current_room = room["outside"].n_to.name
        elif player_1.current_room == room["foyer"].name:
            player_1.current_room = room["foyer"].n_to.name
        elif player_1.current_room == room["narrow"].name:
            player_1.current_room = room["narrow"].n_to.name
        elif player_1.current_room == room["overlook"].name:
            print("you cannot go that way")
    elif player_input == 's':
        if player_1.current_room == room["foyer"].name:
            player_1.current_room = room["foyer"].s_to.name
        elif player_1.current_room == room["overlook"].name:
            player_1.current_room = room["overlook"].s_to.name
        elif player_1.current_room == room["treasure"].name:
            player_1.current_room = room["treasure"].s_to.name
    elif player_input == 'e':
        if player_1.current_room == room["foyer"].name:
             player_1.current_room = room["foyer"].e_to.name
    elif player_input == 'w':
        if player_1.current_room == room["narrow"].name:
            player_1.current_room = room["narrow"].w_to.name
    elif player_input == 'q':
        print('See you next time!')
        break