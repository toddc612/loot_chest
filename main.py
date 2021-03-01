import pandas as pd
import random

def get_monster():
    monsters = pd.read_csv("data/monstats.txt", delimiter="\t")
    monsters.columns = ["class", "type", "level", "treasureclass"]
    rows = monsters.shape[0]
    monster = monsters.iloc[random.randint(0, (rows-1))]
    return monster

def get_base_armor(treasure_class):
    is_item = False

    while not is_item:
        item = get_treasure(treasure_class)

        if item[:2] == 'tc':
            treasure_class = item
            continue
        else:
            is_item = True
            return item

def get_armor_suffix():
    suffixes = pd.read_csv("data/MagicSuffix.txt", delimiter="\t")
    suffixes.columns = ["name", "mod1code",	"mod1min", "mod1max"]
    rows = suffixes.shape[0]
    suffix = suffixes.iloc[random.randint(0, (rows - 1))]
    print("SUFFIX:", suffix)
    return suffix




def get_armor_defense(base_item):
    armor = pd.read_csv("data/armor.txt", delimiter="\t")
    armor.columns = ["name", "minac", "maxac"]
    base = armor.loc[armor['name'] == base_item]
    stats = random.randint(base['minac'].values[0], base['maxac'].values[0])
    return stats

def get_treasure(treasure_class):
    treasures = pd.read_csv("data/TreasureClassEx.txt", delimiter="\t")
    treasures.columns = ["treasureclass", "item1", "item2", "item3"]
    treasure = treasures.loc[treasures['treasureclass'] == treasure_class]
    item = treasure.iloc[:, (random.randint(1, 3))]
    return(item.values[0])


if __name__ == '__main__':
    print('\n--->> Loot Chest v1.0 <<---\n')
    monster = get_monster()
    print("You have slain a ", monster["class"])
    print("TREASURE CLASS:", monster["treasureclass"])
    base_item = get_base_armor(monster["treasureclass"])
    print("BASE ITEM: ", base_item)
    defense = get_armor_defense(base_item)
    print ("DEFENSE:", defense)
    suffix = get_armor_suffix()





