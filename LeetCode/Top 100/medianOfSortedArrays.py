"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""

import sys

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if len(nums2)<len(nums1):
            return self.findMedianSortedArrays(nums2,nums1)
        
        start = 0
        end = len(nums1)
        
        while start<=end:
            partX = int((start+end)/2)
            partY = int((len(nums1)+len(nums2)+1)/2) - partX
            
            maxLeftX = nums1[partX-1] if partX!=0 else -sys.maxsize
            maxLeftY = nums2[partY-1] if partY!=0 else -sys.maxsize
            minRightX = nums1[partX] if partX!=len(nums1) else sys.maxsize
            minRightY = nums2[partY] if partY!=len(nums2) else sys.maxsize

            if maxLeftX<=minRightY and maxLeftY<=minRightX:
                if (len(nums1) + len(nums2))%2==0:
                    return float(max(maxLeftX,maxLeftY)+min(minRightX,minRightY))/2
                else:
                    return float(max(maxLeftX,maxLeftY))
            elif maxLeftX>minRightY:
                end = partX-1
            else:
                start = partX+1
        
        
