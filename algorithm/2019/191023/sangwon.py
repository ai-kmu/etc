테스트 통과
def solution(triangle):
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            
            if j==0:
                triangle[i][j] +=triangle[i-1][j]
            elif j==(len(triangle[i])-1):
                triangle[i][j] +=triangle[i-1][len(triangle[i])-2]
            else:
                triangle[i][j] +=max(triangle[i-1][j-1],triangle[i-1][j])
                
    return max(triangle[-1])   
효율성 테스트 통과 못함
def solution(triangle):
    answer=0
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            
            if j==0:
                triangle[i][j] +=triangle[i-1][j]
            elif j==(len(triangle[i])-1):
                triangle[i][j] +=triangle[i-1][len(triangle[i])-2]
            else:
                triangle[i][j] +=max(triangle[i-1][j-1],triangle[i-1][j])
           answer=max(triangle[-1])    
    return answer   
