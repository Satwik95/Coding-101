#credit:https://www.youtube.com/watch?v=utE_1ppU5DY

def leftRotate():
    no_of_set = gcd(n,k)
    for i in range(no_of_set):
        j = i
        temp = a[i]
        while True:
            d=(j+k)%len(a)
            if d==i:
                break
            a[j]= a[d]
            j=d
        a[j]=temp
            
