# 21. 정수 삼각형 - 프로그래머스

def solution(triangle):
    answer = 0

    # 둘째 줄부터 계산, 첫째 줄 index가 0부터 시작
    for rows in range(1, len(triangle)):
        # 각 줄의 index값 별로 비교
        for idx in range(rows + 1):
            # 가장 왼쪽 값인 경우
            if idx == 0:
                triangle[rows][idx] += triangle[rows - 1][idx]
            # 가장 오른쪽 값인 경우
            elif idx == rows:
                triangle[rows][idx] += triangle[rows - 1][-1]
            else:
                triangle[rows][idx] += max(triangle[rows - 1][idx - 1], triangle[rows - 1][idx])
            print(triangle[rows][idx])
    # 가장 마지막 줄의 최댓값 구하기
    answer = max(triangle[-1])
    return answer

triangle_1 = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle_1))