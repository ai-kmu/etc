"""
RGB거리2
"""

n = int(input())

prices = []
table = [[0 for col in range(3)] for row in range(n)]

for i in range(n):
    r, g, b = map(int, input().split())
    prices.append([r, g, b])

table[0] = prices[0]

"""
table[1][0] = min(table[0][1] + prices[1][0], table[0][2] + prices[1][0])
table[1][1] = min(table[0][0] + prices[1][1], table[0][2] + prices[1][1])
table[1][2] = min(table[0][0] + prices[1][2], table[0][1] + prices[1][2])

Memoization.
"""

for j in range(1, n):
    table[j][0] = min(table[j - 1][1] + prices[j][0], table[j - 1][2] + prices[j][0])
    table[j][1] = min(table[j - 1][0] + prices[j][1], table[j - 1][2] + prices[j][1])
    table[j][2] = min(table[j - 1][0] + prices[j][2], table[j - 1][1] + prices[j][2])

print(min(table[n - 1]))
