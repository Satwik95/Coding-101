class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def bin_search(val, row, col):
            while(row>=0 and col<len(matrix[0])):
                if matrix[row][col]==val:
                    return True
                elif val>matrix[row][col]:
                    col+=1
                else:
                    row-=1
            return False
        return bin_search(target, len(matrix)-1, 0)