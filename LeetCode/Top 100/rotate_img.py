class Solution(object):
    def rotate(self, A):
        n = len(A)
        for i in range(n//2):
            for j in range(n-n//2):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
                         A[~j][i], A[~i][~j], A[j][~i], A[i][j]