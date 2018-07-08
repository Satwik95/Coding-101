def f2(x):
    x=x+1
    print(x)
    return x

def f1(x):
    if x==2:
        return 
    x = 2
    print(x,hex(id(x)))
    f1(x)
    #print(x)
    
x = 0
print(x,hex(id(x)))
z = f1(x)
