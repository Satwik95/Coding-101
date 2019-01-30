def _queue_key(person):
    height, count = person
    return -height, count

def reconstruct_queue_2(people):
    result = []
    new_p = sorted(people, key=_queue_key)
    print(new_p)
    for person in new_p:
        _, count = person
        result.insert(count, person)
    return result

print(reconstruct_queue_2([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
