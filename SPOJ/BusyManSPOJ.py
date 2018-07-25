# your code goes here
def util(x):
    return x[1]

def find_max_act(act):
    sorted_act = sorted(act,key=util)
    count=1
    prev_end_time = sorted_act[0][1]
    for i in range(1,len(sorted_act)): 
        cur_act_start = sorted_act[i][0]
        if cur_act_start>=prev_end_time:
            count+=1
            prev_end_time = sorted_act[i][1]
    return count

if __name__ == "__main__":
    cases = int(input())
    j=1
    result = []
    while j<=cases:
        N = int(input())
        activities = []
        for i in range(0,N):
                m,n = map(int,input().split(" "))
                activities.append([m,n])
        result.append(find_max_act(activities))
        j+=1
    for x in result:
       print(x)
