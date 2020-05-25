#정수 삼각형
#4:00~ 4:38

triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    answer = 0 # 여기서 max 값 갱신할거임

    length=len(triangle)

    for idx1, row1 in enumerate(triangle): # 첫번째 리스트 순회
        endIndex=len(row1)-1
        for idx2, val in enumerate(row1): # 두번째 리스트 순회

            if idx1==0: # 만약 삼각형의 첫번째 행이면
                answer=val # 일단 answer에 대입
                continue

            if idx2==0: # 만약 삼각형의 해당 행의 첫번째 열이면 (삼각형의 왼쪽 사이드면)
                triangle[idx1][0]+=triangle[idx1-1][0] # 해당 위치의 오른쪽 대각선 위만 더해줌
            elif idx2==endIndex: # 만약 삼각형의 해당 행의 첫번째 열이면 (삼각형의 오른쪽 사이드면)
                triangle[idx1][idx2] += triangle[idx1 - 1][idx2-1] # 해당 위치의 왼쪽 대각선 위만 더해줌
            else: # 만약 삼각형의 해당 행의 사이드가 아닌 중간 열이면
                if triangle[idx1 - 1][idx2-1] > triangle[idx1 - 1][idx2]: # 해당 위치의 왼쪽 대각선 위와 오른쪽 대각선 위 비교해서 더 큰거 대입
                    triangle[idx1][idx2]+=triangle[idx1-1][idx2-1]
                else:
                    triangle[idx1][idx2] += triangle[idx1 - 1][idx2]

            currentValue=triangle[idx1][idx2]
            if currentValue>answer: # 더해준 삼각혀으이 값이 지금까지의 값보다 크면
                answer=currentValue  #갱신

    return answer

if __name__ == '__main__':
    solution(triangle)