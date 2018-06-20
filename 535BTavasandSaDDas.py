"""
You are given a lucky number n. Lucky numbers are the positive integers whose decimal representations contain only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

If we sort all lucky numbers in increasing order, what's the 1-based index of n?

Tavas is not as smart as SaDDas, so he asked you to do him a favor and solve this problem so he can have his headphones back.

Input
The first and only line of input contains a lucky number n (1 ≤ n ≤ 109).

Output
Print the index of n among all lucky numbers.

"""
def calc(n):
    x = len(str(n))
    res1 = (1<<x)-2 # 2^x - 2 ---->> reduced from sum of GP formula [a(r^(n-1) - 1)]/[r-1]
    i = 0
    res2 = 0
    while i<x:
        if str(n)[i] == 7:
            index = x - i
            res2 += (1<<(x-i))
        i+=1
        
    return res1 + res2 +1

print(calc(4))
