from cave import Cave
from character import Enemy


cavern = Cave("cavern")
cavern.set_description("A damp and dirty cave.")
grotto = Cave("grotto")
grotto.set_description("A small cave with ancient graffiti.")
dungeon = Cave("dungeon")
dungeon.set_description("A large cave with a rack")

cavern.link_cave(dungeon, "south")
grotto.link_cave(dungeon, "east")
dungeon.link_cave(grotto, "west")
dungeon.link_cave(cavern, "north")

harry = Enemy("Harry", "A smelly Wumpus")
harry.est_conversation("Hangry...Hanggrry")
harry.set_weakness("vegemite")
dungeon.set_character(harry)

current_cave = cavern          
while True:		
    print("\n")         
    current_cave.get_details()         
    command = input("> ")    
    current_cave = current_cave.move(command)
