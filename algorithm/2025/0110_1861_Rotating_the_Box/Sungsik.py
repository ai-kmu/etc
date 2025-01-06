class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])

        answer = [["." for _ in range(m)] for _ in range(n)]

        for row in range(m):
            count = 0
            for col in range(n):
                # stone을 만날때마다 개수를 셈
                if boxGrid[row][col] == "#":
                    count += 1
                # obstacle을 만날때 count 개수만큼 stone으로 설정
                elif boxGrid[row][col] == '*':
                    for k in range(1, count+1):
                        answer[col-k][m-row-1] = '#'
                    answer[col][m-row-1] = '*'
                    count = 0
            for k in range(count):
                answer[n-k-1][m-row-1] = '#'
        
        return answer
