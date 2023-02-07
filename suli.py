szam=-1
x=0
while szam<1 or szam>20:
    szam=int(input("Kérem adjon meg egy számot 1 és 20 között."))
for i in range(szam+1):
    x+=i
print(x)