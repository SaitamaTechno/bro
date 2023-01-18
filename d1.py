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

print(uk["date"][0])
print(wti["date"][0])
wti["date"].pop(832)
wti["date"].pop(1104)
wti["date"].pop(1545)
wti["date"].pop(1883)

uk["date"].pop(1876)
uk["date"].pop(2122)
uk["date"].pop(3087)
popwtilist=[832,1104,1545,1883]
popuklist=[1876,2122,3087]
for i in range(4):
    wti["open"].pop(popwtilist[i])
    wti["close"].pop(popwtilist[i])
for i in range(3):
    uk["open"].pop(popuklist[i])
    uk["close"].pop(popuklist[i])

for i in range(3359):
    if uk["date"][i] != wti["date"][i]:
        print(i)
        break
    print(uk["date"][i], wti["date"][i])
#print(wti["date"][-1])
print(i)
print(uk["date"][i:i+5], wti["date"][i:i+5])

#print(uk.keys()) #Headers of my data
#print(wti.keys())
def cf(change):
    i1=change.find("(")
    i2=change.find("%")
    change=float(change[i1+1:i2].replace("−","-"))
    return change
#print(cf(uk["change"][0]))
#print(cf(wti["change"][0]))

ukopen1=uk["open"][0]
ukcloselist=uk["close"]
wtiopen1=wti["open"][0]
wticloselist=wti["close"]
farklist=[]
for i in range(len(ukcloselist)):
    ukfark=(ukcloselist[i]-ukopen1)/ukopen1
    wtifark=(wticloselist[i]-wtiopen1)/wtiopen1
    farklist.append(ukfark-wtifark)

xpoints = np.array(uk["date"])
ypoints = np.array(farklist)

plt.plot(xpoints, ypoints)
plt.grid()
plt.show()