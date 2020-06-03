def sol():
    num_list = []
    for i in range(0, 11):
        D, V = map(int, input().split(" "))
        num_list.append([D, V])

    num_list.sort()
    #시간과 패널티에 대해 각각 계산이 필요함
    #패널티는 지금까지 쌓인 시간 V * 20을 더해야 하기 때문
    #즉, 패널티는 현 시점에서 더해지지만 시간은 누적됨
    time, penalty = 0, 0
    for D, V in num_list:
        time += D
        penalty += time + (20 * V)
    return penalty
if __name__ == "__main__":
    print(sol())
