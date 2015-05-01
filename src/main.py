from _overlapped import NULL
from os.path import sys

import knowledgeBase as kb
import rules as rules


pokemon_number_map = {"1": kb.get_pokemon("Charizard"), "2": kb.get_pokemon("Sealeo"), "3": kb.get_pokemon("Sand Slash"), "4": kb.get_pokemon("Flygon"), "5": kb.get_pokemon("Venusaur"), "6": kb.get_pokemon("Blastoise")}
compPokemon = kb.all_pokemon
curr_user_pokemon = kb.get_pokemon("Charizard")
curr_comp_pokemon = kb.get_pokemon("Charizard")
    
def generate_pokemon_list():
    for i in range(1, len(kb.all_pokemon)+1):
        print(i, "\t", kb.all_pokemon[i-1].get_name())
       
def choose_pokemon(isComp):
    global curr_comp_pokemon
    global curr_user_pokemon
    global computerPokemon
    if not isComp:
        if len(myPokemon) == 0:
            print("You lost!")
            sys.exit(0)
        print("Which Pokemon do you choose to call?")
        choice = int(input())
        curr_user_pokemon = kb.get_pokemon(myPokemon[choice-1])
        print("Go ", curr_user_pokemon.get_name())
        return;
    else:
        if len(computerPokemon) == 0:
            print("You won!")
            sys.exit(0)
        str = []
        compStrengths = curr_user_pokemon.get_weaknesses()
        for i in range(1, len(computerPokemon)-1):
            tempPokemon = kb.get_pokemon(computerPokemon[i-1])
            for j in range(0, len(compStrengths)):
                str.append(compStrengths[i])
                tempstr =  tempPokemon.get_strengths()
                for i in range(0, len(tempstr)):
                    if i in str:
                        curr_comp_pokemon = tempPokemon
                        print("The computer chose ", curr_comp_pokemon.get_name())
                        return;
        curr_comp_pokemon = kb.get_pokemon(computerPokemon[len(computerPokemon)-1])
        print("The computer chose ", curr_comp_pokemon.get_name())
        return
        
def display_stats():
    global curr_comp_pokemon
    global curr_user_move 
    global name
    movem = curr_user_pokemon.get_moves()
    move1 = movem[0]
    move2 = movem[1]
    move3 = movem[2]
    move4 = movem[3]
    print(name, "\t: ", curr_user_pokemon.get_name(), "\t ", curr_user_pokemon.get_health(), "\n1) ", move1.get_name() , "\t 2) ", move2.get_name(), "\n3) ", move3.get_name(), "\t 4) ", move4.get_name())
    print()
    print("Computer\t: ", curr_comp_pokemon.get_name(), "\t", curr_comp_pokemon.get_health()) 
    
def move_effect(attacker, move, curr_user_pokemon, curr_comp_pokemon):
    global compPokemon
    global myPokemon
    global computerPokemon
    if attacker == "User":
        attackXp = move.get_attack_xp();
        defenceXp = move.get_defence_xp();
        
        if len(curr_user_pokemon.get_type()) > 1:
            if curr_user_pokemon.get_type()[0] in curr_comp_pokemon.get_weaknesses() or curr_user_pokemon.get_type()[1] in curr_comp_pokemon.get_weaknesses():
                attackXp *= 1.2
            elif curr_user_pokemon.get_type()[0] in curr_comp_pokemon.get_type() or curr_user_pokemon.get_type()[1] in curr_comp_pokemon.get_type():
                attackXp *= 0.8
                defenceXp *= 1.2
            curr_user_pokemon.set_defence(int(defenceXp))
            curr_comp_pokemon.set_health(int(curr_comp_pokemon.get_health()-attackXp))
            print(name, " used ", move.get_name(), " ! Computer lost ", int(attackXp), " health")
            if curr_comp_pokemon.get_health() <= 0:
                print("Computer's Pokemon fainted!")
                computerPokemon.remove(curr_comp_pokemon.get_name())
                print(computerPokemon)
                choose_pokemon(True)
            if curr_user_pokemon.get_health() <= 0:
                print("User's Pokemon fainted!")
                myPokemon.remove(curr_user_pokemon.get_name())
                print(myPokemon)
                choose_pokemon(False)
            return
        else:
            if curr_user_pokemon.get_type()[0] in curr_comp_pokemon.get_weaknesses():
                attackXp *= 1.2
            elif curr_user_pokemon.get_type()[0] in curr_comp_pokemon.get_type():
                attackXp *= 0.8
                defenceXp *= 1.2
            curr_user_pokemon.set_defence(int(defenceXp))
            curr_comp_pokemon.set_health(int(curr_comp_pokemon.get_health()-attackXp))
            print(name, " used ", move.get_name(), "! Computer lost ", int(attackXp), " health")
            if curr_comp_pokemon.get_health() <= 0:
                print("Computer's Pokemon fainted!")
                computerPokemon.remove(curr_comp_pokemon.get_name())
                print(computerPokemon)
                choose_pokemon(True)
            if curr_user_pokemon.get_health() <= 0:
                print("User's Pokemon fainted!")
                myPokemon.remove(curr_user_pokemon.get_name())
                print(myPokemon)
                choose_pokemon(False)
            return
    else:
        maxAttack = 0
        maxDefence = 0
        maxMove = 0
        for i in range(0, 4):
            currMovesMany = curr_comp_pokemon.get_moves()
            currMove = currMovesMany[i]
            if maxAttack < rules.calculate_move_effect(curr_comp_pokemon, curr_user_pokemon, currMove):
                maxAttack = rules.calculate_move_effect(curr_comp_pokemon, curr_user_pokemon, currMove)
                maxMove = currMove
        curr_user_pokemon.set_health(int(curr_user_pokemon.get_health()-maxAttack));
        print("Computer used ", currMove.get_name(), "! User lost ", int(maxAttack), " health")
        if curr_user_pokemon.get_health() <= 0:
            print("User's Pokemon fainted!")
            myPokemon.remove(curr_user_pokemon.get_name())
            print(myPokemon)
            choose_pokemon(False)
        if curr_comp_pokemon.get_health() <= 0:
                print("Computer's Pokemon fainted!")
                computerPokemon.remove(curr_comp_pokemon.get_name())
                print(computerPokemon)
                choose_pokemon(True)
        return;
name = input("Enter your name \n")
print("Welcome", name)
compPokemon = rules.calculate_which_pokemon_to_pick(kb.all_pokemon)
computerPokemon = []
for i in range(0, 3):
    computerPokemon.append(compPokemon[i].get_name())
print("The computer has chosen its three Pokemon. It's your turn. Enter three Pokemon numbers from the list")
generate_pokemon_list()
choice1 = input()
choice2 = input()
choice3 = input()
myPokemon = [pokemon_number_map[choice1].get_name(), pokemon_number_map[choice2].get_name(), pokemon_number_map[choice3].get_name()]
print("You chose: \n1) ", myPokemon[0] , "\n2) ", myPokemon[1] , "\n3) ", myPokemon[2])
print("Let the game begin!")
choose_pokemon(False)
choose_pokemon(True)

while True:
    display_stats()
    print("Choose a move")
    curr_user_move = int(input())-1
    movs = curr_user_pokemon.get_moves()
    curr_user_move = movs[curr_user_move]
    move_effect("User", curr_user_move, curr_user_pokemon, curr_comp_pokemon)
    move_effect("Computer", -1, curr_user_pokemon, curr_comp_pokemon)
