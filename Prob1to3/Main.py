import obo
import plotly.graph_objects as go


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele+' '
    return str1

file1 = open('positive.txt')
positive_Word=file1.read()
file1.close()
file2 = open('negative.txt',encoding='utf8')
negative_Word=file2.read()
file2.close()



posiwordlist = positive_Word.split(", ")
negawordlist = negative_Word.split(", ")

def graphAndEvaluation(tf=''):
    file = open(tf, encoding="Latin-1")
    text = file.read()
    file.close()

    fullwordlist = obo.stripNonAlphaNum(text)
    wordlist = obo.rabinKarp1(fullwordlist, obo.stopwords, 101)
    wordlist1 = obo.rabinKarp2(wordlist, posiwordlist, 101)
    wordlist2 = obo.rabinKarp2(wordlist, negawordlist, 101)



    wordString = listToString(wordlist)
    dictionary = obo.wordListToFreqDict(wordlist)
    dictionaryposi = obo.wordListToFreqDict(wordlist1)
    dictionarynega = obo.wordListToFreqDict(wordlist2)
    sorteddict = obo.sortFreqDict(dictionary)
    sorteddictposi = obo.sortFreqDict(dictionaryposi)
    sorteddictnega = obo.sortFreqDict(dictionarynega)

    # for s in sorteddictposi: print(str(s))

    N = 100000
    t = list(dictionary.keys())
    y = list(dictionary.values())
    fig1 = go.Figure(data=go.Scatter(x=t, y=y, mode='markers'))
    fig1.update_layout(title={
        'text': tf + " Word Counts",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
    fig1.show()

    x1 = wordlist1
    x2 = wordlist2

    fig = go.Figure()
    fig.update_layout(title = {
        'text': tf+" Negative and Positive Histogram",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
    fig.add_trace(go.Histogram(histfunc="sum", x=x1, name="Positive Word"))
    fig.add_trace(go.Histogram(histfunc="sum", x=x2, name="Negative Word"))

    fig.show()


def PostiveOrNegative(tf=''):
    file = open(tf, encoding="Latin-1")
    text = file.read()
    file.close()

    fullwordlist = obo.stripNonAlphaNum(text)
    wordlist = obo.rabinKarp1(fullwordlist, obo.stopwords, 101)
    wordlist1 = obo.rabinKarp2(wordlist, posiwordlist, 101)
    wordlist2 = obo.rabinKarp2(wordlist, negawordlist, 101)

    if len(wordlist1)>len(wordlist2):
        return ['Positive',len(wordlist1),len(wordlist2)]
    else:
        return ['Negative',len(wordlist1),len(wordlist2)]

def getPositive(tf):
    file = open(tf, encoding="Latin-1")
    text = file.read()
    file.close()

    fullwordlist = obo.stripNonAlphaNum(text)
    wordlist = obo.rabinKarp1(fullwordlist, obo.stopwords, 101)
    wordlist1 = obo.rabinKarp2(wordlist, posiwordlist, 101)

    return len(wordlist1)



def getNegative(tf):
    file = open(tf, encoding="Latin-1")
    text = file.read()
    file.close()

    fullwordlist = obo.stripNonAlphaNum(text)
    wordlist = obo.rabinKarp1(fullwordlist, obo.stopwords, 101)
    wordlist1 = obo.rabinKarp2(wordlist, negawordlist, 101)

    return len(wordlist1)

couriername=['citylink1.txt','citylink2.txt','citylink3.txt','pos1.txt','pos2.txt','pos3.txt','gdex1.txt','gdex2.txt','gdex3.txt','jnt1.txt','jnt2.txt','jnt3.txt','dhl1.txt','dhl2.txt','dhl3.txt']

if __name__ == "__main__":
    for i in couriername:
        graphAndEvaluation(i)









