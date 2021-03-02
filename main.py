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

def get_armor_prefix():
    prefixes = pd.read_csv("data/MagicPrefix.txt", delimiter="\t")
    prefixes.columns = ["name", "mod1code",	"mod1min", "mod1max"]
    rows = prefixes.shape[0]
    prefix = prefixes.iloc[random.randint(0, (rows - 1))]
    stat = random.randint(int(prefix["mod1min"]), int(prefix["mod1max"]))
    prefix_stat = prefix["mod1code"] + " +" + str(stat)
    return (prefix["name"], prefix_stat)

def get_armor_suffix():
    suffixes = pd.read_csv("data/MagicSuffix.txt", delimiter="\t")
    suffixes.columns = ["name", "mod1code",	"mod1min", "mod1max"]
    rows = suffixes.shape[0]
    suffix = suffixes.iloc[random.randint(0, (rows - 1))]
    stat = random.randint(int(suffix["mod1min"]), int(suffix["mod1max"]))
    suffix_stat = suffix["mod1code"] + " +" + str(stat)
    return (suffix["name"], suffix_stat)

def get_armor_defense(base_item):
    armor = pd.read_csv("data/armor.txt", delimiter="\t")
    armor.columns = ["name", "minac", "maxac"]
    base = armor.loc[armor['name'] == base_item]
    stat = random.randint(base['minac'].values[0], base['maxac'].values[0])
    return stat

def get_treasure(treasure_class):
    treasures = pd.read_csv("data/TreasureClassEx.txt", delimiter="\t")
    treasures.columns = ["treasureclass", "item1", "item2", "item3"]
    treasure = treasures.loc[treasures['treasureclass'] == treasure_class]
    item = treasure.iloc[:, (random.randint(1, 3))]
    return(item.values[0])


if __name__ == '__main__':
    monster = get_monster()
    base_item = get_base_armor(monster["treasureclass"])
    defense = get_armor_defense(base_item)
    (prefix, prefix_stat) = get_armor_prefix()
    (suffix, suffix_stat) = get_armor_suffix()

    print('\n--->> Loot Chest v1.0 <<---\n')
    print("You have slain a ", monster["class"])
    print(prefix + " " + base_item + " " + suffix)
    print ("Defense:", defense)
    print(prefix_stat)
    print(suffix_stat)





