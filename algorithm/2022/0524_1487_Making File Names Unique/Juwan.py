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


        return games.keys()
      
      # 운 좋으면 통과함
"""
Runtime: 9329 ms
Memory Usage: 28.6 MB
"""
