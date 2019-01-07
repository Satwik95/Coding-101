a = [6,2,5,4,5,1,6]

def calcArea(stack, i):
    top = stack.pop(-1)
    if not stack:
        area = a[top]*i
    else:
        area = a[top]*(i-stack[-1]-1)
    return area
        
def largestRec():
    stack = []
    areas = []
    stack.append(0)
    for i in range(1,len(a)+1):
        if i!=len(a):
            if a[i]<=a[stack[-1]]:
                top = a.pop(-1)
            stack.append(i)
        print(areas)
        areas.append(calcArea(stack, i))
    return max(areas)

print(largestRec())
