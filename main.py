import os
import numpy as np
import matplotlib.pyplot as plt

frac = []
init_velo = []
for file in os.listdir("data"):
    with open(file, 'r') as file:
        pass