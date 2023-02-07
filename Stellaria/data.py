def planetname():
  end=0
  import random
  usednames=[]
  
  planetnames=["Gobragawa","Komutis","Zabbao","Liphide","Xunerth","Haivis","Pheilea","Terra","Llelolia","Esunides","Juno","Lalnaunov","Hothion","Tagriea","Tunov","Gaetania","Chohicury","Moduyama","Albedo","Rubedo","Aura","Ainz","Zerota"]
  index=random.randint(0,len(planetnames)-1)
  x=planetnames[index]
  planetnames.pop(index)
  return x
def systems():
  end=0
  import random
  usednames=[]
  while end!=1:
    sysnames=["Glopidrop","Kasik","Genjo","Lennex","Zulu","Ther","Pontifex","Maximus","Fuder","Trickos","Hellas","Manud","Entrolion","Trageda"]
    x=sysnames[random.randint(0,len(sysnames)-1)]
    if x not in usednames:
      usednames.append(x)
      end=1
      return x

def colonynames(index): #unfinished code
  
  clnames=["Alpha","Beta","Gamma","Delta","Epsilon","Zeta","Eta","Theta","Iota"]
  
  return clnames[index]
    