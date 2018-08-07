def twoStacks(x, a, b):
    #
    # Write your code here.
    #
    count=0
    sum=0
    while not not a and not not b:
      if a[0]<b[0]:
        val = a.pop(0)
        print(val)
      else:
        val = b.pop(0)
        print(val)
      sum+=val
      print(sum)
      if sum==x:
        return count+1
      elif sum>x:
          return count
      count+=1
    while sum!=x and not not a:
      sum+=a.pop(0)
      if sum==x:
        return count+1
      elif sum>x:
          return count
      count+=1
    while sum!=x and not not b:
      sum+=b.pop(0)
      if sum==x:
        return count+1
      elif sum>x:
          return count
      count+=1


a = [4, 2, 4, 6, 1]
b = [2, 1, 8, 5]
x = 10
print(twoStacks(x,a,b))
