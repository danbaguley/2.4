from room import Room
from character import Enemy

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")




kitchen = Room("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom = Room("ballroom")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall = Room("dining hall")
dining_hall.set_description("A large room with ornate golden decorations")

#print(kitchen.get_description())

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")

current_room = kitchen
while True:
      print("\n")
      current_room.get_details()
      command = input("> ")
      current_room = current_room.move(command)