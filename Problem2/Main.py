import obo
import plotly.graph_objects as go
import numpy as np

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele+' '
    return str1

file = open('GDEX.txt', encoding="utf8")
text=file.read()
file.close()


fullwordlist = obo.stripNonAlphaNum(text)
wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
wordString = listToString(wordlist)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)

for s in sorteddict: print(str(s))

print("w")

N = 100000
t = list(dictionary.keys())
y = list(dictionary.values())
fig = go.Figure(data=go.Scatter(x=t, y=y, mode='markers'))


fig.show()


