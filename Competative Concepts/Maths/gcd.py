def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
a = int(input())
b = int(input())
print(gcd(a,b))
1 2 5 3 6 4 {<__main__.Node object at 0x7efe1d774128>: 2, <__main__.Node object at 0x7efe1d774160>: 1,
             <__main__.Node object at 0x7efe1d774080>: 1,
             <__main__.Node object at 0x7efe1d774198>: 3, <__main__.Node object at 0x7efe1d7740b8>: 0, <__main__.Node object at 0x7efe1d7741d0>: 2}
