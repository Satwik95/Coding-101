"""
given an array of size n consisting of 1s and 0s,
and k=sum(product of adj pairs),  find in how many combinations will give the
sum pf products equal to k
"""
k=87
mod=1000003
n=100
m=99
dp = [[[0 for i in range(n+1)]for j in range(k)]for y in range(n+1)]
def f(i,prev,count):
    if i==m:
        if count==k:
            return 1
        return 0
    ans=0
    if dp[i][prev][count]!=0:
        return dp[i][prev][count]
    if prev==1:
        ans+=f(i+1,1,count+1)#prev=1, placing 1
    else:
        ans+=f(i+1,1,count)#prev=0,placing 1
    ans%=mod
    ans+=f(i+1,0,count)
    ans%=mod
    dp[i][prev][count]=ans
    return dp[i][prev][count]

print(f(1,0,0)+f(1,1,0))#start by both choice with the first val 0/1
