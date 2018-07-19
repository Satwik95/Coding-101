def sorted(f,a):
    if f<a[0] and len(a)==1:
        return True
    if f<a[0] and sorted(a[0],a[1:len(a)]):
        return True
    else:
        return False

if __name__=="__main__":
    a = [1,6,3,4,5]
    if sorted(a[0],a[1:len(a)]):
        print("Sorted")
    else:
        print("Not Sorted")
