import pandas as pd
import random

def get_monster():
    monsters = pd.read_csv("data/monstats.txt", delimiter="\t")
    rows = monsters.shape[0]
    monster = monsters.iloc[random.randint(0, (rows-1))]
    return monster

def get_base_item(treasure_class):
    # item = get_treasure(treasure_class)
    # print(item)

    is_item = False

    while not is_item:
        item = get_treasure(treasure_class)

        print("ITEM:", item)
        print("PREFIX:", item[:2])
        print("CHECK:", item[:2] == 'tc')

        # If item is prefixed with "tc:", it means references another treasure class
        # so we need to do another lookup with what this value is.

        # Parse "tc:something" to get the class value.

        # If not prefixed with "tc:", then return this value as the base item.

        if item[:2] == 'tc':
            print("MATCHED!\n\n\n")



def get_treasure(treasure_class):
    treasures = pd.read_csv("data/TreasureClassEx.txt", delimiter="\t")
    treasure = treasures.loc[treasures['Treasure Class'] == treasure_class]
    item = treasure.iloc[:, (random.randint(1, 3))]
    return(item.values[0])


if __name__ == '__main__':
    print('\n--->> Loot Chest v1.0 <<---\n')
    monster = get_monster()
    print("MONSTER:", monster["Class"])
    print("TREASURE CLASS:", monster["TreasureClass"])
    base_item = get_base_item(monster["TreasureClass"])



