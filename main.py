
from pokemons import *
from moves import *
from player import Player, characters
import random
import os
import time

# OUVERTURE DU JEU
print("*****************************")
time.sleep(3)
print("*****************************")
time.sleep(2.5)
print("*****************************")
time.sleep(2)
print("*****************************")
time.sleep(1)
print("*****************************")
time.sleep(1)
print("*****************************")
time.sleep(0.5)
print("*****************************")
time.sleep(0.5)
print("*****************************")
time.sleep(0.25)
print("*****************************")
time.sleep(2.5)
os.system('cls')
print("Vous allez combattre violemment et sans pitié des Pokémons")
print()
time.sleep(2)
print("Mais d'abord...")
time.sleep(2.5)
os.system('cls')

# CHOIX DU DRESSEUR
for i, character in enumerate(characters):
    print(f"{i + 1}. {character.name} : {character.inventory}")
print()

while True:
    char_choice = input("Choisissez un dresseur : ")
    if char_choice.isdigit():
        player_choice = int(char_choice) -1

        if 0 <= player_choice <len(characters):
            player_char = characters[player_choice]
            print(f"Vous avez choisi {player_char.name} ?? ")
            time.sleep(1)
            print("Peu importe...")
            time.sleep(1.5)
            print(f"A toi de jouer {player_char.name} !")
            time.sleep(2)
            os.system('cls')

            break
        else:
            print("Choisissez un dresseur.")
            print()
    else:
        print("Choix invalide.")
        print()


is_running = True

# APPARITION DU POKEMON ENNEMI
while is_running:
    pokemon_pnj = random.choice(pokedex)
    print(f"Un {pokemon_pnj.name} sauvage apparait !")
    time.sleep(1.5)
    os.system('cls')

    # POKEMONS DISPONIBLES POUR LE JOUEUR
    print("Pokémons disponibles : ")       
    for i, pokemon in enumerate(pokedex_player):
        print(f"{i + 1} {pokemon.name} : {pokemon.pokemon_type.name}")
    print()

    # CHOIX DU POKEMON PAR LE JOUEUR
    while True: # Verification d'entrée valide
        user_input = (input("Choisissez un Pokémon : "))    

        if user_input.isdigit():
            user_pokemon = int(user_input) - 1 # conversion index

            if 0 <= user_pokemon < len(pokedex_player):
                selected_pokemon = pokedex_player[user_pokemon]
                print(f"Vous envoyez {selected_pokemon.name} au combat !")
                print()
                time.sleep(1)
                break    
        print("Entrée incorrecte.")
        

    # COMBAT
    while selected_pokemon.pv > 0 and pokemon_pnj.pv > 0:
        selected_pokemon.apply_poison() # Créer la possibilité aux pkmns d'avoir un effet poison
        pokemon_pnj.apply_poison()

        # TOUR DU JOUEUR
        print("Attaques : ")
        for i, move in enumerate(selected_pokemon.moves):
            print(f"{i + 1} {move.name}")
        print()
        
        while True: # Vérification d'entrée valide
            player_move = (input("Choisissez une attaque : "))

            if player_move.isdigit():
                player_move_check = int(player_move) - 1

            if 0 <= player_move_check < len(selected_pokemon.moves):
                os.system('cls')
                selected_pokemon.do_moves(player_move_check, pokemon_pnj)
                break
            else:       
                print("Entrée incorrecte")

        if pokemon_pnj.pv <= 0: # Si pokémon pnj est KO
            print(f"{pokemon_pnj.name} est KO ! Vous gagnez le combat.")
            print()

            money_reward = 150 # Gain d'argent
            player_char.money += money_reward
            print(f"Vous gagnez {money_reward} $")
            
            if player_char.ask_rematch():
                    print("Vous marchez dans Pokemon ville, la ville remplie de Pokemon...")
                    time.sleep(2)
                    os.system('cls')
                    print("Quand étonnemment...")
                    time.sleep(2.5)
                    print("Alors que personne ne s'y attendait...")
                    time.sleep(2)
                    os.system('cls')
                    print("C'est juste improbable...")
                    time.sleep(3)
                    os.system('cls')
                    break
            else:
                os.system('cls')
                print("Merci d'avoir joué à Pokemike, à bientôt !")
                time.sleep(3)
                os.system('cls')
                print("petite bite")
                time.sleep(0.5)
                os.system('cls')
                is_running = False
                break
         
        
        if selected_pokemon.pv <= 0: # Si pokémon joueur est KO
            print(f"{selected_pokemon.name} est KO ! Vous perdez le combat.")
            print()

            money_lose = 85 # Perte d'argent
            player_char.money -= money_lose
            print(f"Vous perdez {money_lose}$")

            if player_char.ask_rematch():
                    break
            else:
                os.system('cls')
                print("Yes merci d'avoir joué à mon jeu c'est carré !")
                time.sleep(3)
                os.system('cls')
                print("mais t'as perdu mdr")
                time.sleep(0.5)
                os.system('cls')
                is_running = False
                break
        
        
        # TOUR DU PNJ
        print(f"{pokemon_pnj.name} attaque à son tour !")
        pnj_move = random.choice(pokemon_pnj.moves)
        pnj_move.attack_on(pokemon_pnj, selected_pokemon)
        selected_pokemon.pv = max(0, selected_pokemon.pv) # pour que les pv du pokemon du joueur ne soient pas négatifs

