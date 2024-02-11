import time
import itertools
import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import csv

# The following lines make up the main course of the experiments. 
# We define the dimension of the game we are interested in (d), 
# the number of values per dimension we want to play with (n) and 
# how many games to play. 

start = time.time()
d = 5
n = 3
games = 100000
remainders = []

# Play SET the specified number of times, count how many cards are
# left at the end of each game, and append that value to the list
# "remainders". 

for i in range(games):
    board, completed_sets = lets_play_set(d,n)
    remainders.append(len(board)//n)

# Count how many times each value occurs in the remainders list. 
counter = Counter(remainders)
end = time.time()



# From here onwards, we print a few results to the terminal, make 
# and save a chart and write the summarised results to a CSV file.  

print("runtime: {} seconds".format(round(end - start,4)))
print(counter)

max_bin = max(remainders)
title = "games = {:,}, d = {}, n = {}".format(games,d,n)
suptitle = "How many cards remain?"
plt.hist(remainders, np.arange(max_bin+2)-0.5, ec='k')
plt.locator_params(axis="both", integer=True, tight=True)
plt.xlabel('number of remaining cards divided by 3')
plt.ylabel('frequency')
plt.suptitle(suptitle)
plt.gca().yaxis.set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
plt.title(title)


png_file_name = str(games) + "games__" + str(d) + "d__" + str(n) + "n" + ".png"
plt.savefig(png_file_name)
plt.show()
plt.close()



csv_file_name = str(games) + "games__" + str(d) + "d__" + str(n) + "n" + ".csv"
with open(csv_file_name,'w') as f:
    w = csv.writer(f)
    w.writerows(counter.items())
