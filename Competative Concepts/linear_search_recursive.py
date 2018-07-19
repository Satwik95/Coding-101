""" returning index val"""
def f(a,val):
    global i
    i+=1
    if a==[]: #no items left
        return -1
    if a[0]==val:
        return i
    return f(a[1:len(a)],val)

i=0
a = [1,2,3,4,5]
print(f(a,6))
