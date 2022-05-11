from typing import List, Tuple

_ = input()

cakes : List[Tuple[int, int]] = list(map(lambda x: (x[0], int(x[1])), enumerate(input().split())))

# (index, value)
cumulative: List[Tuple[int, int]] = [(0,0)]*len(cakes)
for i in range(1, len(cakes)):
    cumulative[i] = (cakes[i][0], cumulative[i-1][1] + cakes[i-1][1])
sorted_cakes = sorted(cakes, key=lambda x: (x[1], -x[0]), reverse=True)

# print('cakes', cakes)
# print('sorted cakes', sorted_cakes)
# print('cumulative', cumulative)

holder = 0
score = [0, 0]

next_cake = 0
cumulative_prev_value = 0
i = 0
while i < len(sorted_cakes) and next_cake < len(cakes):
    # print(score)
    index_of_next_biggest, value_of_next_biggest = sorted_cakes[i] 
    # give everything but the biggest value to opponent 
    if value_of_next_biggest >= (cumulative[next_cake][1] - sum(score)):
        score[(holder+1)%2] += cumulative[index_of_next_biggest][1] - sum(score)
        score[holder] += value_of_next_biggest
        # go to the cake we haven't taken
        next_cake = index_of_next_biggest + 1
        # go to the next biggest cake that we haven't taken 
        while i < len(cakes) and sorted_cakes[i][0] < next_cake:
            i += 1
    # else take the current one
    else:
        # take the cake
        score[holder] += cakes[next_cake][1]
        next_cake += 1
    # swap
    holder = (holder + 1)%2

print(score[1], score[0])
