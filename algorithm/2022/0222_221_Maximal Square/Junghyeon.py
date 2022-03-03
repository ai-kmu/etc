class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        brute force 방식으로 2차원 배열을 순회하면서 최댓값을 갱신하는 방식으로 풀이
        '''
        # (0, 0)부터 (m, n)까지 완전 탐색
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if matrix[m][n] == '1':
                    # 초깃값 할당
                    size = 1
                    boolen = True
                    # out of range이거나 false값을 가진 경우에 루프 종료
                    while size + m < len(matrix) and size + n < len(matrix[0]) and boolen:
                        # 루프를 돌면서 0인 지점을 발견하면 루프 탈출
                        for i in range(n, size + n + 1):
                            if matrix[m + size][i] == '0':
                                boolen = False
                                break
                        for j in range(m, size + m + 1):
                            if matrix[j][n + size] == '0':
                                boolen = False
                                break
                        # boolen이 True인 경우 size를 증가시킨다.
                        if boolen:
                            size += 1
                    # result의 최댓값을 업데이트
                    result = max(size, result)
                    
                    # time out을 방지하기위해 result가 가질수 있는 최댓값 일때 강제 종료
                    if result == len(matrix[0]) or result == len(matrix):
                        return result**2
                    
        return result**2
