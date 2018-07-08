def f(nums):
    if len(nums)>=130:
        print("yes")
        return 0
    else:
        for i in range(0,len(nums)):  
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for l in range(k+1,len(nums)):
                        if (nums[i]^nums[j]^nums[k]^nums[l]) == 0:
                            print("yes")
                            return 0


    print("no")
""" using pigeon hole principle, will work for 64 bit integers """
                                                    
                                     
                                                


    
