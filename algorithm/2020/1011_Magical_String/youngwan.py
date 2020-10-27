class Solution:
    def magicalString(self, n: int) -> int:
        answer = 0
        s = [1,2,2]
        ac_s = [1, 2]
        num = 2
        
        while(len(s) < n):
            ac_s.append(s[num])  # s의 원소를 ac_s에 하나 추가
            if (ac_s[num] == 1): # 추가된 원소가 1인 경우
                if(s[-1] == 1):  # 이전 원소에 따라 1 또는 2를 s에 추가
                    s.append(2)
                else:
                    s.append(1)
            else:                # 추가된 원소가 2인 경우
                if(s[-1] == 1):  # 이전 원소에 따라 11 또는 22 추가
                    s += [2,2]
                else:
                    s += [1,1]
            num += 1             # num 1 증가
            
        for i in range(n):       # n만큼의 길이에서 1의 개수 
            if s[i] == 1:
                answer += 1
        return answer
