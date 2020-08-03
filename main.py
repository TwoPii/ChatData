import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.ioff()
from scipy import stats


chat = open("chat.txt")
words = []
for line in chat:
    message = line.split(":")[-1]
    message = message[0: -1]
    linewords = message.split()
    for word in linewords:
        if(word != "<Multimedia" and word != "omitido>" ):
            if(len(word) <= 20):
                words.append(word)

wordMap = {}
for word in words:
    if (wordMap.get(str(word)) != None):
        wordMap[str(word)] += 1
    else:
        wordMap[str(word)] = 1

print(sorted(wordMap.items(), key=lambda x: x[1], reverse=True)[0:20])

x = list(map(len, wordMap.keys()))
y = list(wordMap.values())

sns.regplot(x=x, y=y)
plt.show()
