
from random import randint
import knowledgeBase as kb

hit_probability  = 0

def calculate_move_effect(myPokemon, enemyPokemon, myMove):
    my_strengths = kb.get_strength_from_type(myPokemon.get_type())  
    my_weaknesses = kb.get_weakness_from_type(myPokemon.get_type())
    
    if enemyPokemon.get_type() in my_strengths:
        return int(myMove.get_attack_xp()*1.5)
    elif enemyPokemon.get_type() in my_weaknesses:
        return int(myMove.get_attack_xp()*0.6)
    else:
        return int(myMove.get_attack_xp())
    
def calculate_which_pokemon_to_pick(all_pokemon):
    myPokemon = []
    current_strengths = []
    for i in range(0, 10):
        probability_of_selection = 0.333
        j = randint(0, len(all_pokemon)-1)
        if all_pokemon[j] not in myPokemon:   
            tempStr = kb.get_strength_from_type(all_pokemon[j].get_type())
            probability_of_selection *= len(tempStr)
            for k in range(0, len(tempStr)):
                if tempStr[k] in current_strengths:
                    probability_of_selection /= 1.5
            if i < 5 and probability_of_selection > 50:
                    myPokemon.append(all_pokemon[j])
            elif i in range(5, 8) and probability_of_selection in range(20, 50):
                    if len(myPokemon) <= 2:
                        myPokemon.append(all_pokemon[j])
            elif len(myPokemon) < 3:
                myPokemon.append(all_pokemon[j])
                        
    return myPokemon        

"""
print(calculate_which_pokemon_to_pick(kb.all_pokemon))
"""