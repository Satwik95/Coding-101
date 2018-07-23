"""
Using top down dp, and writing the recurrence in the form of T(n)=T(n/2)
to reach the base case in logn steps
"""
M = 1000000007
h = dict.fromkeys(range(M))
h[0]=1
h[1]=1

def fibo(n):
    if h[n]!=0:
        return h[n]
    
    k = n/2

    if n%2==0:
        h[n] = (fibo(k)*fibo(k) + fibo(k-1)*fibo(k-1))%M
        return h[n]
    else:
        h[n]= (fibo(k)*fibo(k+1) + fibo(k-1)*fibo(k-1))%M
        return h[n]


n = int(input())
fibo(n-1)#f(n) is the n+1th fibo no
print("The nth fibo no is:", h[n-1])
