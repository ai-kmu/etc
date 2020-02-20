def fineMaxTime(N,K):
    MaxTime = K-N
    i = 2
    while(1):
        dist = K - N*i
        if MaxTime <= abs(dist) :
            max_num_list = N*(i) if N != 0 else K+10 #0문제 해결
            return MaxTime, max_num_list
        i += 1

def findtime(N,K):
    if N >= K :
        return (N-K)

    Maxtime, max_num_list = fineMaxTime(N,K)
    lst = [Maxtime+1] * (max_num_list+1)

    # complex case
    for i in range(N+1):
        lst[N-i] = i

    for i in range(N+1, max_num_list+1):
        if i % 2 == 1:
            lst[i] = lst[i-1]+1
        else :
            if lst[i-1]+1 > lst[i//2]:      # /연산을 해서 나오는 것의 자료형은 무조건 float
                lst[i] = lst[i//2]
                for j in range(1,100000):        # 0일때 문제 해결
                    if lst[i-j] > lst[i-j+1]+1:
                        lst[i-j] = lst[i-j+1]+1
                    else : break

            else : lst[i] = lst[i-1]+1
    return lst[K]
    
            
if __name__ == "__main__":
    N, K = map(int, input().split())
    print(findtime(N,K))