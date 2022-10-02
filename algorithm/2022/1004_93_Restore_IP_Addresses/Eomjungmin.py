class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        l = len(s) # 입력 s의 총 길이
        ans = [] # 정답 리스트
        
        # ip 주소에 있는 숫자의 갯수가 아무리 커도 12가 최대 
        if l > 12:
            return ans
        
        # backtracking
        def backtracking(curr_string,i,n_dots):
            if n_dots > 4:
                return
            
            # 점 4개 다 찍었으면 정답 리스트 ans에 추가해서 리턴
            if n_dots == 4 and i == l:
                ans.append(curr_string[:-1])
                return 
            
            # 시작점 i부터 숫자 3개를 보는데 그 3개 안에서 for문 반복
            # for문 반복하면서 현재 보는 string 구간이 256보다 작거나
            # 한자리 숫자, 또는 시작 숫자가 0이 아닌 경우 string에 추가
            for j in range(i, min(i+3, l)):
                if int(s[i:j+1]) < 256 and (i == j or int(s[i]) != 0):
                    backtracking(curr_string+s[i:j+1]+'.',j+1,n_dots+1)
                
        backtracking("",0,0)
        return ans
        
