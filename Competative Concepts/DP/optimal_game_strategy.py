"""
2 smart players, can pick a number only from the ends, alt chance,
how to maximize the win margin
"""
a = [7,3,2,5,8,4]
m = len(a)
dp = [[0 for x in range(m)]for y in range(m)]     
def f(i,j):
    if i>len(a) or j>len(a):
        return 0
    if i>j:
        return 0
    if dp[i][j]!=0:
        return dp[i][j]
    #player one selectes from the ith end
    q1 = a[i]+ min(f(i+2,j),f(i+1,j-1))
    #player one selects from the jth end
    q2 = a[j]+min(f(i,j-2),f(i+1,j-1))
    dp[i][j]=max(q1,q2)
    return dp[i][j]
print(f(0,m-1))

