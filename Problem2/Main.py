import urllib.request, urllib.error, urllib.parse, obo

file = open('JNT.txt', encoding="utf8")
text=file.read()
file.close()


fullwordlist = obo.stripNonAlphaNum(text)
wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)

for s in sorteddict: print(str(s))

import plotly.graph_objects as go
import numpy as np

N = 100000
t = list(dictionary.keys())
y = list(dictionary.values())

fig = go.Figure(data=go.Scatter(x=t, y=y, mode='markers'))

fig.show()