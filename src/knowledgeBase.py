"""This file contains the knowledge base for the project. It is monotonic - all facts remain true irrespective at all times.
All rules are followed at all times. Truth value is T always. It shall not be updated, deleted or otherwise altered
It is propositional logic in that sense
"""
#from abc import ABCMeta, abstractmethod, abstractproperty

all_types = ("Fire", "Water", "Ice", "Flying", "Grass", "Ground")

moves_types_map = {'Fire': [], 'Water': [], 'Ice': [], 'Flying': [], 'Grass': [], 'Ground': []}

types_strengths = {'Fire': ['Water', ], 'Water': ['Ground', ], 'Ice': ['Fire', 'Flying', ], 'Flying':['Water', 'Ground'], 'Grass': ['Ice', ], 'Ground': ['Fire', ]}

types_weaknesses = {'Fire': ['Ice', ], 'Water': ['Fire', ], 'Ice': ['Ground', ], 'Flying': ['Grass', ], 'Grass': ['Water', ], 'Ground': ['Fire', 'Flying']}

all_moves = []

all_pokemon = []

class Move:
    _type = ""
    _name = ""
    _attack_xp = 0
    _defence_xp = 0
    
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name
    
    def get_type(self):
        return self._type
    
    def set_type(self, value):
        self._type = value
        moves_types_map[value].append(self._name)
        all_moves.append(self)
    
    def get_attack_xp(self):
        return self._attack_xp


    def get_defence_xp(self):
        return self._defence_xp  
   

class Pokemon:
    _type = []
    _name = ""
    _moves = []
    _strengths = []
    _weaknesses = []
    _health = 100
    _defence = 20
    
    def __init__(self, name):
        self._name = name
        

    def get_name(self):
        return self._name


    def get_moves(self):
        return self._moves


    def get_strengths(self):
        return self._strengths


    def get_weaknesses(self):
        return self._weaknesses


    def get_type(self):
        return self._type
    
    def get_health(self):
        return self._health
    
    def set_health(self, health):
        self._health = health
    
    def set_moves(self, moves):
        self._moves = moves
        
    def set_defence(self, xp):
        self._defence = xp

#for hybrid pokemon such as fire/flying, their strengths increase and weakness decrease
    def set_type(self, value):
        self._type = value
        self._strengths = get_strength_from_type(value)
        self._weakness = get_weakness_from_type(value)
        all_pokemon.append(self)
        
                
def get_strength_from_type(value):
    str = []
    for i in range(0, len(value)):
            temp_str = types_strengths[value[i]]
            for j in range(0, len(temp_str)):
                str.append(temp_str[j])
    return str

def get_weakness_from_type(value):
    str = []
    for i in range(0, len(value)):
            temp_str = types_strengths[value[i]]
            for j in range(0, len(temp_str)):
                str.append(temp_str[j])
    return str

def get_pokemon(name):
    for i in range(0, len(all_pokemon)):
        if all_pokemon[i].get_name() == name:
            return all_pokemon[i]
        
        

#4 fire moves
fire_breath = Move("Fire Breath")
fire_breath._attack_xp = 60
fire_breath._defence_xp = 20
fire_breath.set_type("Fire")


over_heat = Move("Over Heat")
over_heat._attack_xp = 80
over_heat._defence_xp = -20
over_heat.set_type("Fire")


ember = Move("Ember")
ember._attack_xp = 90
ember._defence_xp = 10
ember.set_type("Fire")


blaze_kick = Move("Blaze Kick")
blaze_kick._attack_xp = 80
blaze_kick._defence_xp = 0
blaze_kick.set_type("Fire")


#4 water moves
surf = Move("Surf")
surf._attack_xp = 80
surf._defence_xp = 0
surf.set_type("Water")


water_gun = Move("Water Gun")
water_gun._attack_xp = 50
water_gun._defence_xp = 20
water_gun.set_type("Water")


bubble_beam = Move("Bubble Beam")
bubble_beam._attack_xp = 70
bubble_beam._defence_xp = 0
bubble_beam.set_type("Water")


hydro_pump = Move("Hydro Pump")
hydro_pump._attack_xp = 100
hydro_pump._defence_xp = -10
hydro_pump.set_type("Water")


#2 ice moves
blizzard = Move("Blizzard")
blizzard._attack_xp = 90
blizzard._defence_xp = 0
blizzard.set_type("Ice")


hail = Move("Hail")
hail._attack_xp = 30
hail._defence_xp = 50
hail.set_type("Ice")


#2 flying moves
fly = Move("Fly")
fly._attack_xp = 80
fly._defence_xp = 50
fly.set_type("Flying")


quick_attack = Move("Quick Attack")
quick_attack._attack_xp = 50
quick_attack._defence_xp = 30
quick_attack.set_type("Flying")


#4 grass moves
cotton_spore = Move("Cotton Spore")
cotton_spore._attack_xp = 90
cotton_spore._defence_xp = -20
cotton_spore.set_type("Grass")


bullet_seed = Move("Bullet Seed")
bullet_seed._attack_xp = 70
bullet_seed._defence_xp = 0
bullet_seed.set_type("Grass")


leaf_blade = Move("Leaf Blade")
leaf_blade._attack_xp = 50
leaf_blade._attack_xp = 30
leaf_blade.set_type("Grass")


vine_whip = Move("Vine Whip")
vine_whip._attack_xp = 80
vine_whip._defence_xp = 0
vine_whip.set_type("Grass")


#4 ground moves
earthquake = Move("Earthquake")
earthquake._attack_xp = 100
earthquake._defence_xp = -30
earthquake.set_type("Ground")


mud_sport = Move("Mud Sport")
mud_sport._attack_xp = 20
mud_sport._defence_xp = 60
mud_sport.set_type("Ground")


mud_shot = Move("Mud Shot")
mud_shot.__attack_xp = 60
mud_shot._defence_xp = 30
mud_shot.set_type("Ground")


dig = Move("Dig")
dig._attack_xp = 40
dig._defence_xp = 60
dig.set_type("Ground")



#Pokemon

charizard = Pokemon("Charizard")
charizard._moves = [fire_breath, ember, fly, blaze_kick]
charizard.set_type(["Fire", "Flying"])


sealeo = Pokemon("Sealeo")
sealeo._moves =[blizzard, hail, surf, water_gun]
sealeo.set_type(["Ice", "Water"])


sandslash = Pokemon("Sand Slash")
sandslash._moves = [earthquake, mud_sport, mud_shot, dig]
sandslash.set_type(["Ground"])


flygon = Pokemon("Flygon")
flygon._moves = [mud_sport, mud_shot, fire_breath, ember]
flygon.set_type(["Ground", "Fire"])


venusaur = Pokemon("Venusaur")
venusaur._moves = [cotton_spore, bullet_seed, vine_whip, leaf_blade]
venusaur.set_type(["Grass"])


blastoise = Pokemon("Blastoise")
blastoise._moves = [surf, water_gun, bubble_beam, hydro_pump]
blastoise.set_type(["Water"])


#debugging
"""
print(all_pokemon)
print(all_moves)
"""