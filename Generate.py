""" Generate.py

Will hopefully generate a nice 1000*1000 block world to walk on,
then pickle it and store it in a file.
"""
from random import choice
import pickle

types = [0,1,2]
world = []

for i in range(1000):
    world.append([])
    for n in range(1000):
        world[i].append(choice(types))

name = raw_input("Input filename then press enter, please.\n")
with open(name + ".wld", 'w') as f:
    pickle.dump(world, f)
