# LES ATTAQUES ET LEURS DIFFERENTS PARAMETRES

from pokemon_types import FEU, EAU, PLANTE, TERRE, NORMAL, POISON
from pokemon_types import type_advantage
import time
import os


class Moves:
    def __init__(self, name, pokemon_type, damages, applies_poison = False, poison_damage=0, healing_pts=0):
        self.name = name
        self.pokemon_type = pokemon_type
        self.damages = damages
        self.applies_poison = applies_poison
        self.poison_damage = poison_damage 
        self.healing_pts = healing_pts

    def attack_on(self, from_player, target):
        if self.healing_pts > 0: # Si l'attaque est un soin
            if from_player.pv == from_player.max_pv: # Si les pv sont déjà au max
                print(f"Les PV de {from_player.name} sont déjà au maximum.")
                print()
                return

            # Applique le soin    
            healed_amount = min(self.healing_pts, from_player.max_pv - from_player.pv)
            from_player.pv += healed_amount
            print(f"{from_player.name} utilise {self.name}")
            print(f"{from_player.name} récupère {healed_amount} PV")
            print(f"{from_player.name} : {from_player.pv}/{from_player.max_pv}")
            print()
            return
        

        print(f"{from_player.name} lance l'attaque {self.name} !") # Si l'attaque est offensive
        time.sleep(1)

        # Avantage de type
        advantage = type_advantage(self.pokemon_type, target.pokemon_type)
        total_attack = self.damages + from_player.pokemon_type.buffAtt + advantage - target.pokemon_type.buffDef
        total_attack = max(total_attack, 0) # pour que les dégats ne soient pas négatifs

        target.pv = max(0, target.pv - total_attack) # pour que les pv du pnj ne soient pas négatifs

        if advantage > 0:
            print("C'est super efficace") 
            time.sleep(1)      
        elif advantage < -3:
            print("Ce n'est pas très efficace")
            time.sleep(1.5)
        print(f"{target.name} perd {total_attack} PV...")
        time.sleep(1)
        print(f"{target.name} : {target.pv}/{target.max_pv}")
        print()
        time.sleep(2)
        

        # Effet de poison
        if self.applies_poison:
            target.poison_str = self.poison_damage
            target.effect_turns = 5 # Applique un effet poison durant x tours
            if target.pv <= 0:
                print(f"Le poison a eu raison de {target.name}... {target.name} est KO")
                time.sleep(1.5)
                print("Vous gagnez le combat !")
                is_running = False                        
                

        
        

