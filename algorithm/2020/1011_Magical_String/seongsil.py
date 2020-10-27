class Solution:
    def magicalString(self, n: int) -> int:
        S = [1, 2, 2]
        dic = {1:2, 2:1}  # 이전값이 1이면 2로, 2이면 1로 추가
        
        ind = 2
        
        if n >= 3:
            i = 2
            while i <= n: 
                S.extend([dic[S[i]]] * S[ind])   # S[ind]개수 만큼 추가
                i += S[ind]
                ind += 1
                
        print(S)
        return S[:n].count(1) if n > 0  else 0
