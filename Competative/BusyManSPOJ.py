def takeSecond(elem):
    return elem[1]

def find_max_act(act):
    sorted_act = sorted(act,key=takeSecond)
    count=1
    for i in range(0,len(sorted_act)-1): 
        cur_end = sorted_act[i][1]
        print(cur_end)
        next_act_start = sorted_act[i+1][0]
        print(next_act_start)
        if next_act_start>=cur_end:
            count+=1
    return count

if __name__ == "__main__":
    T = int(input())
    while T:
        N = int(input())
        activities = []
        for i in range(0,N):
                n = int(input())
                m = int(input())
                activities.append([n,m])
        max_act = find_max_act(activities)
        print("Max no of activities = ",max_act)
