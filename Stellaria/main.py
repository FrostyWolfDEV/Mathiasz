import random
import data

over=0
class System:
  def __init__(self):
    self.name=data.systems()
    self.planets=random.randint(4,9)
  def GetSystemName(self):
    return self.name
class Planet(System):
  def __init__(self):
    over=0
    temp=0
    x=data.planetname()
    while over!=1:
       
      for i in range(1,len(dict)+1):
        temp=dict.get(str(i))
      if temp!=x:
        self.name=x
        over=1
      else:
        print(f"Reasigned name from {x}")
        x=data.planetname()
    self.habitable=random.randint(0,1)
    self.scanned=0
    x=systems.get(str(keysys))

    self.system=x.GetSystemName()
    #self.id=1
class Colony():
  def __init__(self,planet,suffix) -> None:
    self.planet=planet
    

    self.suffix=suffix
    self.name=planet+self.suffix
    
    
  

print("Stellaria by FrostyWolfDEV")
end=0
keyx=0
keysys=0
keycolony=0
isdev=0
dict={}
found=0
enginelevel=1
isdev=1
correntsys=keysys
correntplanet="1"
systems={}
colonyes={}
inventory={"colonykit":10} #inicialise the inventory

def Make_Planet(keyx):
  keyx+=1
  p=Planet() 
  dict[str(keyx)]=p
  
  return keyx
def Make_Sys(keysys):
  keysys+=1
  system=System()
  systems[str(keysys)]=system
  
  return keysys
def Make_Colony(keycolony):
  keycolony+=1
  asd=0
  
  for i in range(len(colonyes)):
    x=colonyes.get(str(i))
    if correntplanet in x:
      asd+=1
  asd=data.colonynames(asd)
  a=Colony(correntplanet,suffix=asd)
  colonyes[str(keycolony)]=a
  return keycolony
  

keysys=Make_Sys(keysys) #make solarsys

x=systems.get(str(keysys)) 
print()
for i in range(x.planets): # make planets for solarsys
  keyx=Make_Planet(keyx)


#keyx=Make_Planet(keyx)
print("Welcome user to your own spaceship. The goal of the game is to make a successful space empire and become the rule of the galaxy. But watch out. You are not the only one who wants to rule everything.")
empire_name=input("What do you want to call your empire?: ")
corrsysname=systems.get(str(keysys))
corrplanet=dict.get(str(keyx))
print(f"You are currently in the system: {corrsysname.name}, above the planet {corrplanet.name}")
print()




while end!=1:
  userinp=input("Command: ")
  if userinp=="EXIT":
    end=1
  elif userinp=="Dev ON":
    isdev=1
  elif userinp=="dev.MP" and isdev==1:
    p=Planet()
    
    dict[str(keyx)]=p
    keyx+=1
  elif userinp=="dev.check" and isdev==1:
    
    #print(p.name)
    #print(p.habitable)
    #print(p.id)
    #print(dict.get("0"))     Id: 0 doesn't exist anymore. 
    #print(dict.get("1"))
    for i in range(1,len(dict)+1):
      #print(i)
      x=dict.get(str(i))
      #print(dict)
      print(x.name)
      print(x.system)
    x=dict.get(correntplanet)
    for i in range(1,len(colonyes)+1):
      x=colonyes.get(str(i))
      print("Colony:",x.planet , x.name)

    x=dict.get(correntplanet)
    print(f"Curr planet: {correntplanet} , {x.name}")

      
  elif userinp=="dev.checkname" and isdev==1:
    print(data.planetname())
  
  elif userinp=="dev.DMP" and isdev==1:
    keyx=Make_Planet(keyx)
  elif userinp=="Scan":
    target=input("Target? ")
    temp=0
    found=0
    if target=="All":
      
      x=systems.get(str(keysys))

      print(f"All planets in the {x.name} system:")
      for i in range(1,len(dict)+1):
        x=dict.get(str(i))
        print(f"{i} {x.name}")
        x.scanned=1
    else:
      for i in range(1,len(dict)+1):
        x=dict.get(str(i))
        
        
        if x.name==target:
          print(f"Planet {target} was found. It is:")
          if x.habitable==1:
              print("Habitable")
          else:
              print("Inhabitable")
          x.scanned=1
          found=1
      if found!=1:
        print(f"No planet by the name {target} was found!")
  elif userinp=="Shiplogs":   #shiplogs
    print("We have the folowing logs:")
    print("Planets\n") 
    if len(colonyes)>0:
      print("Colonyes") 
    log=input(("Which log do you want to access?: "))
    if log=="Planets":
        print("We know the planets:\n")
        for i in range(1,len(dict)+1):
            x=dict.get(str(i))
            print(x.name)
            
            if x.scanned==1:
              if x.habitable==1:
                print("It is habitable")
                print("-"*10)
              else:
                print("It is inhabitable")
                print("-"*10)
    if log=="Colonyes" and len(colonyes)>0:
      if i in range(1,len(colonyes)+1):
        x=colonyes.get(str(i))
        print(x.name)
  elif userinp=="Move":
    x=systems.get(str(keysys))
    print(f"As our engine is only level 1 we cannot move outside the solarsystem. There are only {x.planets} plants in this system. ")
    target=input("Where do you want to move?")
    found=0
    for i in range(1,len(dict)+1):
      x=dict.get(str(i))
      if x.name==target:
        print("We have arrived at the destination.")
        correntplanet=str(i)
        found=1
    if found!=1:
      print(f"We found no planet called: {target}")
  elif userinp=="Colonise":
    if inventory.get("colonykit")>0:
      x=dict.get(str(correntplanet))
      print(f"Do you want to colonise the planet {x.name}")
      inp=input("(Y)es or (N)o?")
      if inp=="Y":
        keycolony=Make_Colony(keycolony)
        
        inventory.update({"colonykit":inventory.get("colonykit")-1})
      else:
        print("Colonising process stopped.") 
              
                

