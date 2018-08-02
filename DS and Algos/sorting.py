class Sort:
    
    def merge(self,nums,left,right):
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                nums[k]=left[i]
                i+=1
                k+=1
            else:
                nums[k]=right[j]
                j+=1
                k+=1
        while i<len(left):
            nums[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            nums[k]=right[j]
            j+=1
            k+=1
                
    def MergeSort(self,nums):
        mid = int(len(nums)/2)
        if len(nums)<2:
            return
        left = [x for x in nums[:mid]]
        right = [x for x in nums[mid:]]
        self.MergeSort(left)
        self.MergeSort(right)
        self.merge(nums,left,right)
    
    def SelectionSort(self,nums):
        for i in range(0,len(nums)-1):
            imin = i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[imin]:
                    imin = j
            temp = nums[i]
            nums[i]=nums[imin]
            nums[imin]=temp
        return nums

    def BubbleSort(self,nums):
        for k in range(len(nums)-1):
            flag=0
            for i in range(len(nums)-k-1):
                if nums[i]>nums[i+1]:
                    temp = nums[i+1]
                    nums[i+1]=nums[i]
                    nums[i]=temp
                    flag=1
            #if already sorted then there will be no more swapping
            if flag==0:
                break
        return nums

    def InsertionSort(self,nums):
        for unsorted_part in range(1,len(nums)):
            hole = unsorted_part
            value = nums[hole]
            while hole>0 and nums[hole-1]>value:
                nums[hole]=nums[hole-1]
                hole=hole-1
            nums[hole]=value
        return nums

if __name__=="__main__":
    s = Sort()
    nums = [8,9,4,7,3,6]
    s.MergeSort(nums)
    print(nums)
