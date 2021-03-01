import pandas as pd
import random

def get_monster():
    monsters = pd.read_csv("data/monstats.txt", delimiter="\t")
    monsters.columns = ["class", "type", "level", "treasureclass"]
    rows = monsters.shape[0]
    monster = monsters.iloc[random.randint(0, (rows-1))]
    return monster

def get_base_item(treasure_class):
    is_item = False

    while not is_item:
        item = get_treasure(treasure_class)

        if item[:2] == 'tc':
            treasure_class = item
            continue
        else:
            is_item = True
            return item

def get_item_stats(base_item):
    armor_stats = pd.read_csv("data/armor.txt", delimiter="\t")



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
    base_item = get_base_item(monster["treasureclass"])
    print("BASE ITEM: ", base_item)
    item_stats = get_item_stats(base_item)





