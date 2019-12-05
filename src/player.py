# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.current_room = current_room
        self.name = name
        self.items = []
    
    def on_take(self, command):
        for it in self.current_room.items:
            if it == command[1]:
                self.current_room.items.remove(command[1])
                self.items.append(command[1])
                print(f'you now have {command[1]} in your items.')
            else:
                print(f'{command[1]} is not in this room!')
    
    def on_drop(self, comm):
        for it in self.items:
            if it == comm[1]:
                self.items.remove(comm[1])
                self.current_room.items.append(comm[1])
                print(f'you now have dropped {comm[1]} item.')
            else:
                print(f'{comm[1]} not in your list of items!')