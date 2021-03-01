import pandas as pd
import random

def get_monster():
    monsters = pd.read_csv("data/monstats.txt", delimiter="\t")
    monsters.columns = ["class", "type", "level", "treasureclass"]
    rows = monsters.shape[0]
    monster = monsters.iloc[random.randint(0, (rows-1))]
    print(monster)



if __name__ == '__main__':
    print('\n--->> Loot Chest v1.0 <<---\n')
    get_monster()


