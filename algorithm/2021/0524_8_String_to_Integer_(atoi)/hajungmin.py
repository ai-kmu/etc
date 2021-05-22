class Solution:
    def myAtoi(self, s: str) -> int:
        # lstrip을 통해 왼쪽 공백을 없애주고 리스트화 시켜준다.
        s_new = s.lstrip()
        s_new = list(s_new)
        #정답을 저장해줄 result를 선언해준다.
        result = ""
        
        if not s_new: return 0
        
        #만약 처음 시작이 +나 -라면 이 후의 리스트 요소를 탐색하며 숫자인 경우 result에 더해준다.
        if (s_new[0] == "+") or (s_new[0] == "-"):
            result += s_new[0]
            if len(s_new) == 1: return 0
            for i in s_new[1:]:
                if i == "+" or i == "-":
                    break
                if i.isdigit():
                    result += i
                else: break
        
        # 처음 시작이 알파벳이라면 0을 return 해줌
        if s_new[0].isalpha():
            return 0

        # 처음 시작이 숫자라면 이후 숫자가 아닌 요소가 나올 때까지 result에 더해준다.
        if s_new[0].isdigit():
            for i in s_new:
                if i.isdigit():
                    result += i
                else: break
                
        # 예외 요소로 result에 아무것도 없거나 result에 +나 -만 저장된 경우에 0을 return 해준다.
        if not result: return 0
        if result == "+" or result == "-": return 0

        # 결과를 int형으로 변형시켜준다
        result_int = int(result)

        # 최대, 최소 범위를 벗어난 경우 최대 최소값을 return 해준다.
        if result_int > 2147483647: return 2147483647
        if result_int < -2147483648: return -2147483648

        # 결과를 return 해준다.
        else: return result_int
