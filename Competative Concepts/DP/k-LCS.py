def kLCS(i,j,k):
    if i==len(str1) or j==len(str2):
        # if any string is covered, so there will
        # be 0 common part left
        return 0
    if dp[i][j][k]!=-1:
        return dp[i][j][k]
    res = 0
    if str1[i]==str2[j]:
        res = 1+kLCS(i+1,j+1,k)
    else:
        # change ith char
        if k>0:
            res = max(res,1+kLCS(i+1,j+1,k-1))
        q2 = kLCS(i,j+1,k)
        q3 = kLCS(i+1,j,k)
        res = max(res,q2,q3)
    dp[i][j][k] = res
    return dp[i][j][k]

if __name__=="__main__":
    str1 = input()
    str2 = input()
    k = int(input())
    dp = [[[-1 for l in range(k+1)] for j in range(len(str2)+1)]for i in range(len(str1)+1)]
    print(kLCS(1,1,k))
