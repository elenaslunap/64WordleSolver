import numpy as np
import pandas as pd

word_file = pd.read_fwf("../data/wordle-answers-alphabetical.txt")
juegos = pd.DataFrame()

for i in range(10000):
    juego = np.random.choice(word_file, size = 64, replace = False)
    juegos = pd.concat([juegos, pd.DataFrame(juego)], axis = 0)

juegos.to_csv("../data/juegos.csv")




