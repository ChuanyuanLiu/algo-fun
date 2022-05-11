# Maximum weight independent set, assumes input is a path graph / aka stick
from typing import List

n : int = int(input())
graph : List[int] = [int(input()) for i in range(n)]

# Memorization
padding = 2
A: List[int] = [0]*(n+padding)

for i, v in enumerate(graph):
    index = i+padding
    A[index] = max(A[index-1], v + A[index-2])

# retrace solution
picked = ['0']*len(A)
i = len(A) - 1
while i > 0:
    # case 1, we pick A[i]
    if (graph[i-padding] + A[i-2] >= A[i-1]):
        picked[i] = '1'
        i-=2
    # case 2, we don't pick A[i]
    else:
        i-=1
# print(graph)

assert(sorted(A) == A)
assert(sum(map(lambda x: x[0], filter(lambda x: x[1] == '1', zip(graph, picked[padding:])))) == A[-1])

indexes = [1,2,3,4,17,117,517,997]
print("".join([picked[i+padding-1] for i in indexes]))
