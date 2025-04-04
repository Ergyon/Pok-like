
from moves import Moves
from pokemon_types import *

# ATTAQUES DISPONIBLES

# Feu
LANCE_FLAMME = Moves("Lance Flamme", FEU, 80)
INCENDIE = Moves("Incendie", FEU, 45)
BRIQUET = Moves("Briquet", FEU, 25)
# Eau
LANCE_EAU = Moves("Lance eau", EAU, 85)
INNONDATION = Moves("Innondation", EAU, 50)
ROBINET = Moves("Robinet", EAU, 25)
# Plante
LANCE_PLANTE = Moves("Lance plante", PLANTE, 90)
MOISSONAGE = Moves("Moissonage", PLANTE, 50)
TRUELLE = Moves("Truelle", PLANTE, 20)
# Terre
LANCE_TERRE = Moves("Lance terre", TERRE, 80)
TUNNEL = Moves("Tunnel", TERRE, 50)
COUP_DE_PELLE = Moves("Coup de pelle", TERRE, 30)
# Poison
CYANURE = Moves("Cyanure", POISON, 45, applies_poison=True, poison_damage=25)
PET_FOIREUX = Moves("Pet foireux", POISON, 70, applies_poison=True, poison_damage=20)
LEVER_DE_BRAS = Moves("Lever de bras", POISON, 70, applies_poison=True, poison_damage=15)
PEC_CITRON = Moves("Pec citron", POISON, 35, applies_poison=True, poison_damage=5)
# Vent
TORNADE = Moves("Tornade", VENT, 85)
VENT_AILE = Moves("Vent ailé", VENT, 45)
CLAQUE_PORTE = Moves("Claque porte", VENT, 25)
# Foudre
ZEUS_HAND = Moves("Zeus hand", FOUDRE, 95)
DECHARGE = Moves("Décharge", FOUDRE, 30)
AMPEREMETRE = Moves("Ampèremètre", FOUDRE, 15)



# Normal
UPPERCUT = Moves("Uppercut", NORMAL, 40)
NIPPON = Moves("Nippon", NORMAL, 35)
HIGH_KICK = Moves("High Kick", NORMAL, 40)
BALAYETTE = Moves("Balayette", NORMAL, 30)
GRIFFURE = Moves("Griffure", NORMAL, 35)
MORSURE = Moves("Morsure", NORMAL, 30)
DOLIPRANE = Moves("Doliprane", NORMAL, damages=0, healing_pts=40)
MORPHINAX = Moves("Morphinax", NORMAL, damages=0, healing_pts=60)
CROC_EN_JAMBE = Moves("Croc en jambes", NORMAL, 50)

