print("Enter the larger string")
t = input()
print("Enter the smaller string")
s = input()
i=0
res = any(s==t[i:i+len(s)]for i in range((len(t)-len(s))+1))
if res:
    print("Yes there is a match!")
else:
    print("No there is no match")
