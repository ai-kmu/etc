from collections import deque


class Solution(object):
    def decodeString(self, s):

        s = deque(s)
        
        # 숫자가 나오면 숫자를 next_times에 몇번 반복할지를 저장
        # (stack을 이용)
        # '['가 나오면 함수를 제귀적으로 호출
        # ']'가 나오면 함수를 반환
        
        def decoder(times, s):
            answer = ""
            tmp = ""
            while s:
                next_times = ""
                # 숫자가 나올경우
                if 48 <= ord(s[0]) and ord(s[0]) <= 57:
                    while s[0] != "[":
                        next_times += s.popleft()
                    # '['를 제거
                    s.popleft()
                    # 함수 제귀적으로 호출
                    answer += decoder(int(next_times),s)
                # ']'가나올경우
                elif s[0] == "]":
                    s.popleft()
                    for _ in range(times): 
                        tmp += answer   
                    return tmp
                # 나머지 경우(괄호 밖의 경우)
                else:
                    answer += s.popleft()
                    
            return answer
        
        return decoder(1, s)
