class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        s_length = len(s)
        p_length = len(p)
        
        # p와 s dictionary 초기화
        dict_p = [0 for i in range(26)]
        dict_s = [0 for i in range(26)]
        for i in p:
            dict_p[ord(i)-97] += 1
            
        count = 0
        
        # for loop in s
        for i in range(s_length):                
            # 만약 p에 없는 문자일 경우 0으로 초기화하고 다시 시작
            if dict_p[ord(s[i])-97] == 0:
                count = 0
                dict_s = [0 for i in range(26)]
                continue
            else:
                # count가 p_length를 넘었을 때 그 전의 문자를 한번 지워야함.
                if count >= p_length and dict_s[ord(s[i-p_length])-97] != 0:
                    dict_s[ord(s[i-p_length])-97] -= 1
                    count -= 1
                # i번째 문자의 count를 +1 함.
                dict_s[ord(s[i])-97] += 1
                count += 1
                
                # 만약 count가 p length가 됐다면 검사 가능(아니면 아직 채워야함.)
                if count == p_length:
                    flag = True
                    for j in range(26):
                        if dict_p[j] != dict_s[j]:
                            flag = False
                            break
                    if flag:
                        answer.append(i-p_length+1)

        
        return answer
