'''
[feedback]
dictionary에 지금까지 등장한 중복된 이름을 value로 갱신하면 Time Error 해결 가능(한줄)
=> cnt를 정의했지만 games[i]는 항상 1부터 탐색을 시작해서 진행 / 중복된 이름 key에 대한 value 값을 1씩 증가함으로써 위에 문제 해결
'''

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        games = defaultdict(lambda : 0) # 딕셔너리 생성
        
        for i in names:
            if games[i] == 0: # 만약 딕셔너리에 없다면
                games[i] += 1 # 딕셔너리에 추가

            else: # 만약 있으면
                cnt = games[i]

                while(games[f'{i}({cnt})']): # 이미 생성한 폴더가 있는 지 확인. 없으면 while 탈출
                    cnt += 1
                s = f'{i}({cnt})'
                games[s] += 1
                games[i] += 1  # 수정코드 1

        return games.keys()
      
      # 운 좋으면 통과함
"""
Runtime: 9329 ms
Memory Usage: 28.6 MB
"""
