# DEFINITION D'UN POKEMON ET DE SES ATTRIBUTS

from pokemon_types import EAU, FEU, PLANTE, TERRE, NORMAL
from pokemon_types import type_advantage
from moves import Moves
from attacks_list import *

class Pokemon:
    def __init__(self, name, pv, pokemon_type, moves):
        self.name = name
        self.pv = pv
        self.max_pv = pv # Empêche que les soins ne fassent dépasser les pv max
        self.pokemon_type = pokemon_type
        self.moves = moves 
        self.effect_turns = 0 # Compte la durée des effets en tours
        self.poison_str = 0 # Degats de poison propres à chaque attaque
        self.heal_str = 0 # Point de guérison selon les attaques


    def apply_poison(self): # Applique l'effet de poison
        if self.effect_turns > 0:
            self.pv = max(0, self.pv - self.poison_str)
            self.effect_turns -= 1 # Réduit le nombre de tours restants de l'effet
            print(f'{self.name} subit {self.poison_str} dégâts de poison...')
            print(f"{self.name} : {self.pv} PV")
            print()

            if self.pv == 0:
                print(f"Le poison a eu raison de {self.name}... {self.name} est KO.")
                print("Vous gagnez le combat !")
                return True
        return False

    def is_healing(self): # Soigne le pokémon
        self.pv = max(0, self.pv + self.heal_str)
            

    def do_moves(self, moves_id, pokemon): 
        if 0 <= moves_id < len(self.moves):
            selected_move = self.moves[moves_id]
            selected_move.attack_on(self, pokemon)
        else:
            print("Vous devez sélectionner une attaque.")

    def defense(self, attack, type_attack):
        return attack - self.pokemon_type.buffDef - (type_advantage(self.pokemon_type, type_attack))    


# POKEMONS DISPONIBLES 
# Feu
nekfeu = Pokemon("Nekfeu", 200, FEU, [LANCE_FLAMME, INCENDIE, HIGH_KICK, UPPERCUT])
volcanax = Pokemon("Volcanax", 211, FEU, [LANCE_FLAMME, LANCE_TERRE, NIPPON, DOLIPRANE])
cheminee = Pokemon("Cheminée", 163, FEU, [BRIQUET, LANCE_FLAMME, CROC_EN_JAMBE, DOLIPRANE])
# Eau
nekwater = Pokemon("Nekwater", 220, EAU, [LANCE_EAU, INNONDATION, CROC_EN_JAMBE, NIPPON])
carafe = Pokemon("Carafe", 194, EAU, [INNONDATION, MORPHINAX, UPPERCUT, BALAYETTE])
piscinator = Pokemon("Piscinator", EAU, 171, [ROBINET, LANCE_EAU, DOLIPRANE, BALAYETTE])
# Plante
nekplante = Pokemon("Nekplante", 240, PLANTE, [LANCE_PLANTE, MOISSONAGE, DOLIPRANE, BALAYETTE])
racinos = Pokemon("Racinos", 198, PLANTE, [LANCE_PLANTE, DOLIPRANE, MORSURE, HIGH_KICK])
jardiniere = Pokemon("Jardinière", PLANTE, 155, [LANCE_PLANTE, TRUELLE, CYANURE, GRIFFURE])
# Terre
nekterre = Pokemon("Nekterre", 230, TERRE, [LANCE_TERRE, TUNNEL, NIPPON, HIGH_KICK])
crevasse = Pokemon("Crevasse", 249, TERRE, [LANCE_TERRE, TUNNEL, NIPPON, DOLIPRANE])
# Poison
nekpoison = Pokemon("Nekpoison", 217, POISON, [CYANURE, UPPERCUT, PET_FOIREUX, TUNNEL])
mekensueur = Pokemon("Mekensueur", 280, POISON, [PET_FOIREUX, LEVER_DE_BRAS, UPPERCUT, MORSURE])
# Vent
bigoiseau = Pokemon("Bigoiseau", 221, VENT, [TORNADE, VENT_AILE, GRIFFURE, MORSURE])
nuage_gris = Pokemon("Nuage gris", 186, VENT, [TORNADE, VENT_AILE, LEVER_DE_BRAS, NIPPON])
# Normal
bonhomme = Pokemon("Bonhomme", 207, NORMAL, [MORPHINAX, UPPERCUT, VENT_AILE, BALAYETTE])
madame = Pokemon("Madame", 232, NORMAL, [MORPHINAX, BALAYETTE, HIGH_KICK, DOLIPRANE])


pokedex_player = [nekfeu,
                  nekplante,
                  nekwater,
                  nekterre,
                  nekpoison]


pokedex =   [nekfeu,
    nekwater,
    nekplante,
    nekterre,
    nekpoison,
    mekensueur,
    bigoiseau,
    bonhomme,
    racinos,
    carafe,
    volcanax,
    nuage_gris,
    crevasse,
    madame,
    cheminee,
    piscinator,
    jardiniere,
]


