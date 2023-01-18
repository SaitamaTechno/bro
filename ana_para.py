import json
import matplotlib.pyplot as plt
import numpy as np

f=open("UKOIL.json", "r")
a=json.load(f)
f.close()
uk=json.loads(a)

f=open("WTICOUSD.json", "r")
a=json.load(f)
f.close()
wti=json.loads(a)

print(uk["change"][0], uk["date"][0])
print(wti["change"][0], wti["date"][0])

#print(uk.keys()) #Headers of my data
#print(wti.keys())
def cf(change):
    i1=change.find("(")
    i2=change.find("%")
    change=float(change[i1+1:i2].replace("−","-"))
    return change

print(cf(uk["change"][0]))
print(cf(wti["change"][0]))

popwtilist=[832,1104,1545,1883]
popuklist=[1876,2122,3087]
for i in range(4):
    wti["date"].pop(popwtilist[i])
    wti["open"].pop(popwtilist[i])
    wti["close"].pop(popwtilist[i])
    wti["change"].pop(popwtilist[i])
for i in range(3):
    uk["date"].pop(popuklist[i])
    uk["open"].pop(popuklist[i])
    uk["close"].pop(popuklist[i])
    uk["change"].pop(popuklist[i])
    
bank=1000
uk_money=500
wti_money=500

banklist=[]
for i in range(len(uk["change"])):
    e=cf(uk["change"][i])
    g=cf(wti["change"][i])
    if i+1 in range(len(uk["change"])):
        if (g-e) > 1.8: #1
            if cf(wti["change"][i]) > cf(uk["change"][i]):
                wti_money -= wti_money * ((wti["close"][i]-wti["close"][i+1])/wti["close"][i])
                uk_money += uk_money * ((uk["close"][i]-uk["close"][i+1])/uk["close"][i])
            elif cf(wti["change"][i]) < cf(uk["change"][i]):
                wti_money += wti_money * ((wti["close"][i]-wti["close"][i+1])/wti["close"][i])
                uk_money -= uk_money * ((uk["close"][i]-uk["close"][i+1])/uk["close"][i])
        elif (g-e) < -1.8: #-1
            if cf(wti["change"][i]) > cf(uk["change"][i]):
                wti_money -= wti_money * ((wti["close"][i]-wti["close"][i+1])/wti["close"][i])
                uk_money += uk_money * ((uk["close"][i]-uk["close"][i+1])/uk["close"][i])
            elif cf(wti["change"][i]) < cf(uk["change"][i]):
                wti_money += wti_money * ((wti["close"][i]-wti["close"][i+1])/wti["close"][i])
                uk_money -= uk_money * ((uk["close"][i]-uk["close"][i+1])/uk["close"][i])
        bank = wti_money + uk_money
        banklist.append(bank)
    
uk["date"].pop(-1)
xpoints = np.array(uk["date"])
ypoints = np.array(banklist)

plt.plot(xpoints, ypoints)
plt.grid()
plt.show()