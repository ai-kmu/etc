# 발표자 comment
# 딱히 수정해야할 부분은 안보이지만 굳이 따지자면 PEP(Python Enhancement Proposal) 형식에 따라 주석은 줄맞춤을 해주는것이 좋을것 같습니다.

    
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        m, n = len(matrix), len(matrix[0])
        # 방문 했는지 체크
        visit = [[False for _ in range(n)] for _ in range(m)]
        mn = m*n
        cnt = 0 # element 개수만큼만 수행
        direct = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 방향 right, down, left, up
        curr = {'dir': 0, 'pos': (0, 0)} # 현재 상태
        
        while cnt < mn: # m*n번 탐색
            r, c = curr['pos']
            visit[r][c] = True
            answer.append(matrix[r][c]) # 방문
            cnt += 1
            
            # 다음 pos로 업데이트
            next_r, next_c = r+direct[curr['dir']][0], c+direct[curr['dir']][1]
            if 0 > next_r or 0 > next_c or next_r > m-1 or next_c > n-1 or visit[next_r][next_c]: # 범위를 벗어나거나, 방문했으면 방향틀기
                curr['dir'] = (curr['dir'] + 1) % 4
                next_r, next_c = r+direct[curr['dir']][0], c+direct[curr['dir']][1]
            curr['pos'] = (next_r, next_c)
                
        return answer
