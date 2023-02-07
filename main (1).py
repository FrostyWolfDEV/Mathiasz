import random
seedx=0
ok=0
random.seed(seedx)
while ok!=1 :
  x=random.randint(0,10000000)
  if x==111:
    print("seed:",seedx)
    print("num:",x)
    ok=1
  else:
    seedx=seedx+1
    print("seed:",seedx)
    print("num:",x)