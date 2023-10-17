# def travel(mask, current):
#     if mask == (1 << N) - 1:
#         if cost[current][0] != 0:
#             return cost[current][0]
#         return float('inf')

#     if dp[mask][current] != -1:
#         return dp[mask][current]

#     minimum_cost = float('inf')

#     for i in range(N):
#         if not (mask & (1 << i)) and cost[current][i] != 0:
#             current_cost = cost[current][i] + travel(mask | (1 << i), i)
#             minimum_cost = min(minimum_cost, current_cost)

#     dp[mask][current] = minimum_cost
#     return minimum_cost

# N = int(input())
# cost = [list(map(int, input().split())) for _ in range(N)]
# dp = [[-1] * N for _ in range(1 << N)]

# minimum = travel(1, 0)  # 시작 도시 0으로 고정, 방문 상태 1로 시작
# print(minimum)


def travel(start, visited):
    if len(visited) == N:
        if cost[start][0] != 0:
            return cost[start][0]
        return float("inf")

    minimum_cost = float("inf")

    for i in range(N):
        if cost[start][i] != 0 and i not in visited:
            visited.append(i)
            current_cost = cost[start][i] + travel(i, visited)
            visited.pop()
            minimum_cost = min(minimum_cost, current_cost)

    return minimum_cost

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
visited = [0]

minimum = travel(0, visited)
print(minimum)







# [
#     [0,10,15,20],
#     [5,0,9,10],
#     [6,13,0,12],
#     [8,8,9,0]
# ]