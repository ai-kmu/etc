"""
    우선 문제를 푸는데 시간이 걸리지 않는 것 부터 풀어야 한다.
    여러번 더해지는 것이 적을 수록 유리해지기 때문이다.
"""

def solution(input):
    input.sort()
    price = 0
    T = 0
    for i in input:
        T += i[0]
        price += T + 20*i[1]
    return price

arr = []
for i in range(11):
    D, V = map(int, input().split(" "))
    arr.append([D,V])
print(solution(arr))
