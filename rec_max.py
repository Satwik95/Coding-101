def rec_max(n):
    if len(n)==1:
        return n[0]
    cur = n[0]
    val = rec_max(n[1:])
    if cur>val:
        val=cur
    return val

print(rec_max([5,10,1,2,7,8]))
