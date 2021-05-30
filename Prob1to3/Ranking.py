import Main


customerdistancefromhub1 = [61, 40, 41, 86, 29]
customerdistancefromhub2 = [46, 36, 54, 76, 34]
customerdistancefromhub3 = [78, 35, 54, 37, 55]
totalcustomerdistancefromhub1 = 0
totalcustomerdistancefromhub2 = 0
totalcustomerdistancefromhub3 = 0
probabicustdistancehub1 = ["","","","",""]
probabicustdistancehub2 = ["","","","",""]
probabicustdistancehub3 = ["","","","",""]


customerpositivewords1 = [4,5,7,3,3]
customerpositivewords2 = [7,9,5,3,5]
customerpositivewords3 = [5,3,6,7,3]
totalcustomerpositivewords1=0
totalcustomerpositivewords2=0
totalcustomerpositivewords3=0
probabicustpostword1 = ["","","","",""]
probabicustpostword2 = ["","","","",""]
probabicustpostword3 = ["","","","",""]


customernegativewords1 = [9,9,9,2,4]
customernegativewords2 = [5,6,7,3,6]
customernegativewords3 = [9,3,1,5,3]
totalcustomernegativewords1=0
totalcustomernegativewords2=0
totalcustomernegativewords3=0
probabicustnegaword1 = ["","","","",""]
probabicustnegaword2 = ["","","","",""]
probabicustnegaword3 = ["","","","",""]


sentimenthub=["","","","",""]

for x in range(5):
    totalcustomerdistancefromhub1 = totalcustomerdistancefromhub1+customerdistancefromhub1[x]
    totalcustomerdistancefromhub2 = totalcustomerdistancefromhub2+customerdistancefromhub2[x]
    totalcustomerdistancefromhub3 = totalcustomerdistancefromhub3 + customerdistancefromhub3[x]
    totalcustomerpositivewords1 = totalcustomerpositivewords1 + customerpositivewords1[x]
    totalcustomerpositivewords2 = totalcustomerpositivewords2 + customerpositivewords2[x]
    totalcustomerpositivewords3 = totalcustomerpositivewords3 + customerpositivewords3[x]
    totalcustomernegativewords1 = totalcustomernegativewords1 + customernegativewords1[x]
    totalcustomernegativewords2 = totalcustomernegativewords2 + customernegativewords2[x]
    totalcustomernegativewords3 = totalcustomernegativewords3 + customernegativewords3[x]

for x in range(5):
     probabicustdistancehub1[x] = 1-(customerdistancefromhub1[x] / totalcustomerdistancefromhub1)
     probabicustdistancehub2[x] = 1-(customerdistancefromhub2[x] / totalcustomerdistancefromhub2)
     probabicustdistancehub3[x] = 1-(customerdistancefromhub3[x] / totalcustomerdistancefromhub3)

     probabicustpostword1[x] = (customerpositivewords1[x] / totalcustomerpositivewords1)
     probabicustpostword2[x] = (customerpositivewords2[x] / totalcustomerpositivewords2)
     probabicustpostword3[x] = (customerpositivewords3[x] / totalcustomerpositivewords3)

     probabicustnegaword1[x] = 1-(customernegativewords1[x] / totalcustomernegativewords1)
     probabicustnegaword2[x] =1-(customernegativewords2[x] / totalcustomernegativewords2)
     probabicustnegaword3[x] = 1-(customernegativewords3[x] / totalcustomernegativewords3)





print(probabicustpostword1)
print(probabicustpostword2)
print(probabicustpostword3)
print(probabicustnegaword1)
print(probabicustnegaword2)
print(probabicustnegaword3)
print(sentimenthub)
print(Main.PostiveOrNegative('pos1.txt'))