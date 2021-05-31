import Main

customerdistancefromhub1 = [61, 40, 41, 86, 29]
customerdistancefromhub2 = [46, 36, 54, 76, 34]
customerdistancefromhub3 = [78, 35, 54, 37, 55]
totalcustomerdistancefromhub1 = 0
totalcustomerdistancefromhub2 = 0
totalcustomerdistancefromhub3 = 0
probabicustdistancehub1 = [""]*5
probabicustdistancehub2 = [""]*5
probabicustdistancehub3 = [""]*5

couriername=['citylink1.txt','citylink2.txt','citylink3.txt','pos1.txt','pos2.txt','pos3.txt','gdex1.txt','gdex2.txt','gdex3.txt','jnt1.txt','jnt2.txt','jnt3.txt','dhl1.txt','dhl2.txt','dhl3.txt']
courierposiword=[0]*5
k=0
for i in range(15):
    if i != 0 and i%3==0:
        k+=1
    courierposiword[k]+=Main.getPositive(couriername[i])

print(list(courierposiword))


couriernegaword=[0]*5
k=0
for i in range(15):
    if i != 0 and i%3==0:
        k+=1
    couriernegaword[k]+=Main.getNegative(couriername[i])

print(list(couriernegaword))




totalhubpositivewords1=0
probabihubpostword1 = ["","","","",""]




totalhubnegativewords1=0
probabihubnegaword1 = ["","","","",""]

sentimenthub=["","","","",""]
totalprobability =0
totalsentimenthub =0

portklangranking=0
petalingjayaranking=0
batucavesranking=0
kajangranking=0
sungaibulohranking=0


for x in range(5):
    totalcustomerdistancefromhub1 = totalcustomerdistancefromhub1+customerdistancefromhub1[x]
    totalcustomerdistancefromhub2 = totalcustomerdistancefromhub2+customerdistancefromhub2[x]
    totalcustomerdistancefromhub3 = totalcustomerdistancefromhub3 + customerdistancefromhub3[x]
    totalhubpositivewords1 = totalhubpositivewords1 + courierposiword[x]
    totalhubnegativewords1 = totalhubnegativewords1 + couriernegaword[x]

for x in range(5):
     probabicustdistancehub1[x] = 1-(customerdistancefromhub1[x] / totalcustomerdistancefromhub1)
     probabicustdistancehub2[x] = 1-(customerdistancefromhub2[x] / totalcustomerdistancefromhub2)
     probabicustdistancehub3[x] = 1-(customerdistancefromhub3[x] / totalcustomerdistancefromhub3)

     probabihubpostword1[x] = (courierposiword[x] / totalhubpositivewords1)
     probabihubnegaword1[x] = 1-(couriernegaword[x] / totalhubnegativewords1)

for x in range(5):
    totalprobability= totalprobability+probabicustdistancehub1[x]+probabicustdistancehub2[x]+probabicustdistancehub3[x]+probabihubpostword1[x]+probabihubnegaword1[x]
for x in range(5):
    sentimenthub[x] = (probabicustdistancehub1[x]+probabicustdistancehub2[x]+probabicustdistancehub3[x]+probabihubpostword1[x]+probabihubnegaword1[x])/totalprobability
for x in range(5):
    totalsentimenthub = totalsentimenthub+sentimenthub[x]

newsentimenthub = sentimenthub.copy()

def merge_list(a, b):
    out = []
    while len(a) and len(b):
        if a[0] < b[0]:
            out.append(a.pop(0))
        else:
            out.append(b.pop(0))
    out += a
    out += b
    return out


def strand(a):
    i, s = 0, [a.pop(0)]
    while i < len(a):
        if a[i] > s[-1]:
            s.append(a.pop(i))
        else:
            i += 1
    return s


def strand_sort(a):
    out = strand(a)
    while len(a):
        out = merge_list(out, strand(a))
    return out

sortedlistofprobability = strand_sort(sentimenthub)
for x in range(5):
    for y in range(5):
         if newsentimenthub[x]==sortedlistofprobability[y]:
             if x == 0:
                 portklangranking=y+1
             if x == 1:
                 petalingjayaranking=y+1
             if x == 2:
                 batucavesranking=y+1
             if x == 3:
                 kajangranking=y+1
             if x == 4:
                 sungaibulohranking=y+1


print("probability for hub citylink is :"+str(newsentimenthub[0]))
print("probability for hub pos is :"+str(newsentimenthub[1]))
print("probability for hub gdex is :"+str(newsentimenthub[2]))
print("probability for hub jnt is :"+str(newsentimenthub[3]))
print("probability for hub dhl is :"+str(newsentimenthub[4]))

print("the sorted list of probability is "+ str(sortedlistofprobability))
print("citylink is number "+str(portklangranking))
print("pos is number "+str(petalingjayaranking))
print("gdex is number " +str(batucavesranking))
print("jnt is number " + str(kajangranking))
print("dhl is number "+ str(sungaibulohranking))