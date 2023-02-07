# Írjunk egy programot ami bekéri egy felhasználótól 10 nevét,életkorát és a kedvenc ételét majd azokat beleírja egy fájlba
#A fájlban mindíg új sorban kezdődjön az új névvel kezdődő sor
#Megoldás
"""
file=open("szemet.txt","w",encoding="UTF-8")
for i in range(2):
    nev=input("Kérem andja meg a nevet: ")
    kor=input("Kérem adja meg az életkorát: ")
    kaja=input("Kérem adja meg a kedvenc ételét: ")
    writable=nev+" "+kor+" "+kaja+"\n"
    file.write(writable)
file.close()
"""
#Kérjönk be a felhasználótól egy számot 1 és 100 között. Ezt addik kérjük be amíg a szám nem felel meg. Ha a felhasználó jó számot ad meg akkor generáljunk egy random számor a megadott szám és 250 között. A generált számból vonjuk ki a bekért számot. Ezek utánn nézzük meg hogy a kapott szám páros vagy páratlan-e. Ha páros akkor írjuk ki egy fájlba a bekért számot és azt hogy páros. Ha páratlan akkor írjuk ki a fájlba a generált számot és azt hogy páratlan.

"""
import random
szam=-1
while szam<0 or szam>100:
    szam=int(input("Kérem adjon meg egy számot 1 és 100 között: "))
randomszam=random.randint(szam,250)
file=open("szemet.txt","w",encoding="UTF-8")
if randomszam-szam%2==0:
    file.write(str(szam)+" "+"Páros")
else:
    file.write(str(randomszam)+" "+"Páratlan")
"""
#Kérjünk be a felhasználótól egy számot és írjuk ki a megadott számig a pozitív egész számok összegét. Pl. 9-et ad meg a felhasználó, akkor 1+2+3+4+5+6+7+8+9=45. Ezt az összedást irjuk bele egy fájlba ez eredményével együtt.
x=0
szam=-1
while szam<0:
    szam=int(input("Kérem adjon meg egy pozitív egész számot: "))
for i in range(1,szam+1):
    
    x+=i
print(f"A számok összege: {x}")
