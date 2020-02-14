def findMin(lst, houseN, colorN, mincost, cost, N,firstC) :
    cost += lst[houseN][colorN]
    if houseN == N-1:
        if cost < mincost[0] and firstC != colorN :
            mincost[0] = cost
    else:
        for i in range(3) : #https://ychae-leah.tistory.com/48
            if i != houseN :
                findMin(lst, houseN+1, i, mincost, cost,N,firstC)
        





if __name__ == "__main__":
    lst = []
    N=int(input())
    for i in range(N):
        rC, gC, bC = map(int, input().split())
        lst.append([rC, gC, bC])
   
    mincost = [1001]
    cost = 0
    for j in range(3):
        findMin(lst, 0, j, mincost, cost, N,j)
    print(mincost[0])