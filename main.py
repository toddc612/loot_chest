import pandas as pd
import random

def intro(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.

def get_monster():
    monsters = pd.read_csv("data/monstats.txt", delimiter="\t")
    monsters.columns = ["class", "type", "level", "treasureclass"]
    rows = monsters["class"].count()

    # print(monsters.iloc[1])
    print(monsters["class"].count())


if __name__ == '__main__':
    intro('PyCharm')
    get_monster()


