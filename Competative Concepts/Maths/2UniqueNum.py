def uniqueNums(x,y,nums):
    xor = nums[0]
    
    for i in range(1,len(nums)):
        xor^=nums[i]

    rightmost_setbit = xor&~(xor-1)

    for i in range(0,len(nums)):
        if (nums[i] & rightmost_setbit):
            x^=nums[i]
        else:
            y^=nums[i]
            
    
x=y=0
n = int(input())
inputs = [None]*n
for i in range(0,n):
  inputs[i]=int(input())
  
uniqueNums(x,y,inputs)
print(str(x)+" "+str(y))
