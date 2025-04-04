# PERSONNAGES DISPONNIBLES ET LEURS ACTIONS 
class Player:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
        self.money = 0
        
    def ask_rematch(self): # Demande de rejouer
            while True:
                try:
                    rematch = input("Lancer un nouveau combat ? (o/n) ").lower()
                    if rematch == "o":
                        return True
                    elif rematch == "n":
                        return False
                    else:
                        print("Entrée invalide. Veuillez choisir O u N.")
                except ValueError:
                    print("Entrée incorrecte.")

    def add_item(self, item): # Obtenir des objet (à faire)
        self.inventory.append(item)

    def earn_money(self, amount): # Gagner de l'argent
        self.money += amount

# PERSONNAGES
char1 = Player("Jerem", inventory=["Potion", "Poké Ball"])
char2 = Player("Nico", inventory=["AttackBoost", "Poké Ball"])

characters = [char1, char2]