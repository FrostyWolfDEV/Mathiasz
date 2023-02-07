goal=int(input("Hány hétig tartott a fogyókúra?"))
goalkg=float(input("Elérni kívánt testtömeg(kg): "))
kgs=[]
reached=False
fails=0
for i in range(1,goal+1):
    inp=input(str(i)+". héten=")
    kgs.append(float(inp))
    if float(inp)<=goalkg and reached==False:
        reached=i
for i in range(len(kgs)):
    if i>0:
        if kgs[i-1]<kgs[i]:
            fails+=1
if reached!=False:
    print(f"Mari néni a {reached}.-edik héten érte el a célt. ")
else:
    print("Mari néni sajnos nem érte el a célját.")
if fails>=1:
    print(f"A tömeg {fails} esetben nőtt egyik hétről a másikra")