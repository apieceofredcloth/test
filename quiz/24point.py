from pprint import pprint

cached = {
}

def points_by(seq):
    if num in cached: return cached[num]

    candidate = [max(current,current * largest_multi(num - current))
                 for current in range(1, num + 1)]
    max_ = max(candidate) if candidate else 0
    cached[num] = max_

    return max_

n = 7
print('largest_multi of %s'%n)
pprint(largest_multi(n))
pprint(cached)















def sf():
    pass
