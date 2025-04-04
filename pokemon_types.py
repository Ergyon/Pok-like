# LES DIFFERENTS TYPES, ATTRIBUABLES AUX POKEMONS

class Type:
    def __init__(self, name, buffAtt, buffDef):
        self.name = name
        self.buffAtt = buffAtt        
        self.buffDef = buffDef

EAU = Type("EAU", 6, 6)
FEU = Type("FEU", 6, 7)
PLANTE = Type("PLANTE", 4, 7)
TERRE = Type("TERRE", 4, 8)
NORMAL = Type("NORMAL", 1, 1)
POISON = Type("POISON", 3, 6)
VENT = Type("VENT", 8, 5)
FOUDRE = Type("FOUDRE", 5, 5)

# AVANTAGE OU DESAVANTAGE DE TYPE SUR UN AUTRE

def type_advantage(type_att, type_def):
    # Faiblesses feu
    if type_att.name == "EAU" and type_def.name == "FEU":
        return 30
    elif type_att.name == "TERRE" and type_def.name == "FEU":
        return 30
    # Faiblesses plante
    elif type_att.name == "FEU" and type_def.name == "PLANTE":
        return 30
    elif type_att.name == "POISON" and type_def.name == "PLANTE":
        return 30
    elif type_att.name == "VENT" and type_def.name == "PLANTE":
        return 30
    # Faiblesses terre
    elif type_att.name == "PLANTE" and type_def.name == "TERRE":
        return 30
    elif type_att.name == "VENT" and type_def.name == "TERRE":
        return 30
    # Faiblesses eau
    elif type_att.name == "PLANTE" and type_def.name == "EAU":
        return 30
    elif type_att.name == "FOUDRE" and type_def.name == "EAU":
        return 30
    # Faiblesses vent
    elif type_att.name =="FOUDRE" and type_def.name =="VENT":
        return 30
    elif type_att.name == "POISON" and type_def.name == "VENT":
        return 30
    # Faiblesses poison
    elif type_att.name =="VENT" and type_def.name == "POISON":
        return 30
    elif type_att.name == "FEU" and type_def.name == "POISON":
        return 30
    # Faiblesses foudre
    elif type_att.name == "TERRE" and type_def == "FOUDRE":
        return 30   
    
        
    elif type_att.name == type_def.name:
        return -40
    else:
        return 0
    