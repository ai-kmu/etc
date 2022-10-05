# 풀이실패...
def solution(N, number):
    answer = 0
    def aug(x,r,answer):
        answer = answer + r
        return int(str(x) * r)
    def div(x,d,answer):
        answer = answer + 1
        return x//d

    # 나올수 있는 경우의 수:
    # n/n = 1
    # n*n = n^2
    # nn...n/n = 11...1
    # n+n = 2n
    # nn...nn - n..n = 10^len(우변) * n
    number = div((aug(N,2,answer) + N),N,answer)
    
    print(answer)
    
    
    
    
    return answer
