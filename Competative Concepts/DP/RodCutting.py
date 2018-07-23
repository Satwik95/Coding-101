import sys
sys.setrecursionlimit(1500)
l=4
dp = [0]*(l+1)
len_wise_profit = {1:2,2:3,3:2,4:5}

def maxProfit_bu(l):
    best=0
    for length in range(1,l+1):
        for cut in range(1,length+1):
            best = max(best,len_wise_profit[cut]+dp[length-cut])
    dp[l]=best
    return dp[l]

def maxProfit(l):
    if l==0:
        return 0
    if dp[l]!=0:
        return dp[l]
    best = 0
    for cut_len in range(1,l+1):
        cur_profit= len_wise_profit[cut_len]+maxProfit(l-cut_len)
        best = max(best,cur_profit)
    dp[cut_len]=best
    return best

print(maxProfit(l))
print(maxProfit_bu(l))
