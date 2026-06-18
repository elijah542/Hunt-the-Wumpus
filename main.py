from cave import Cave
from character import Enemy
from character import Character
dead = False


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
harry.set_conversation("Hangry...Hanggrry")
harry.set_weakness("vegemite")
dungeon.set_character(harry)

current_cave = cavern          
while dead == False:		
    print("\n")         
    current_cave.get_details()         
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")    
    current_cave = current_cave.move(command)

    if command == "talk":
        if inhabitant is not None:
            inhabitant.talk()

    if command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Bravo,hero you won the fight!")
                current_cave.set_character(None)
            else:
                print("Scurry home, you lost the fight.")
                print("That's the end of the game")
                dead = True
        else:
            print("There is no one here to fight with")


