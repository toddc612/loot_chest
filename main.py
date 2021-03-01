import pandas as pd
import random

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


monsters = pd.read_csv("data/monstats.txt", delimiter="\t")
print(monsters.iloc[1])
