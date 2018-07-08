def preComputePrime():
    
    for i in range(3,n+1,2):
        if p[i]:
            for j in range(i*i,n+1,i):
                p[j] = 0

    p[0] = p[1] = 0
    
    for i in range(4,n+1,2):
        p[i] = 0

def findNthPrime():
  preComputePrime()
  count = 1
  for i in range(3,n+1,2):
    if p[i]:
      count+=1
      if count == val:
        print(i)
      

val = int(input())
n = 1000000

if val==1:
  print(2)
else:
  p = [1]*(n+1)
  findNthPrime()
