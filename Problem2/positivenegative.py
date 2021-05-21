import obo
import Main


file = open('positive.txt', encoding="utf8")
positive_Word=file.read()
file.close()

file = open('negative.txt', encoding="utf8")
negative_Word=file.read()
file.close()

posiwordlist = obo.stripNonAlphaNum(positive_Word)
negawordlist = obo.stripNonAlphaNum(negative_Word)
print(list(negawordlist))
word1=[]
word2=[]



print(word1)
print(word2)









