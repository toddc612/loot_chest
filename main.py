import pandas as pd
import random

def get_monster():
    monsters = pd.read_csv("data/monstats.txt", delimiter="\t")
    monsters.columns = ["class", "type", "level", "treasureclass"]
    rows = monsters.shape[0]
    monster = monsters.iloc[random.randint(0, (rows-1))]
    return monster

def get_base_item(treasure_class):
    treasures = pd.read_csv("data/TreasureClassEx.txt", delimiter="\t")
    treasures.columns = ["treasureclass", "item1", "item2", "item3"]
    treasure = treasures.loc[treasures["treasureclass"] == treasure_class]
    print(treasure)



if __name__ == '__main__':
    print('\n--->> Loot Chest v1.0 <<---\n')
    monster = get_monster()
    print("MONSTER:", monster["class"])
    print("TREASURE CLASS:", monster["treasureclass"])
    base_item = get_base_item(monster["treasureclass"])



