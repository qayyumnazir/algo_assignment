import obo
import plotly.graph_objects as go
import numpy as np

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele+' '
    return str1

file = open('/Users/hazimaziz/Documents/GitHub/algo_assignment/Problem2/positive.txt')
positive_Word=file.read()
file.close()
file = open('/Users/hazimaziz/Documents/GitHub/algo_assignment/Problem2/negative.txt')
negative_Word=file.read()
file.close()



posiwordlist = positive_Word.split(", ")
negawordlist = negative_Word.split(", ")

file = open('/Users/hazimaziz/Documents/GitHub/algo_assignment/Problem2/JNT.txt',encoding="utf8")
text=file.read()
file.close()


fullwordlist = obo.stripNonAlphaNum(text)
wordlist=obo.rabinKarp1(fullwordlist, obo.stopwords,101)
wordlist1=obo.rabinKarp2(wordlist, posiwordlist,101)
wordlist2=obo.rabinKarp2(wordlist,negawordlist,101)

print(list(wordlist))
print(list(wordlist1))
print(list(wordlist2))



wordString = listToString(wordlist)
dictionary = obo.wordListToFreqDict(wordlist)
dictionaryposi = obo.wordListToFreqDict(wordlist1)
dictionarynega = obo.wordListToFreqDict(wordlist2)
sorteddict = obo.sortFreqDict(dictionary)
sorteddictposi = obo.sortFreqDict(dictionaryposi)
sorteddictnega = obo.sortFreqDict(dictionarynega)

for s in sorteddictposi: print(str(s))

N = 100000
t = list(dictionary.keys())
y = list(dictionary.values())
fig1 = go.Figure(data=go.Scatter(x=t, y=y, mode='markers'))
fig1.show()

x1 = wordlist1
x2 = wordlist2

fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="sum",x=x1, name="Positive Word"))
fig.add_trace(go.Histogram(histfunc="sum",x=x2, name="Negative Word"))

fig.show()







