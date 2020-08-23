# 풀이 규칙
# numRows = 4인 경우
# 0 6 12 18 -> 6씩 증가       -> 6 0 6 0
# 1 5 7 11 13 -> 4 2씩 증가   -> 4 2 4 2
# 2 4 8 10 14 -> 2 4씩 증가   -> 2 4 2 4
# 3 9 15 21 -> 6씩 증가       -> 0 6 0 6
# 2*(numRows - 1[#1] - 첫 번째 위치의 숫자), 2*(첫 번째 위치의 숫자) 의 규칙으로 증가함
#1. 1을 뺀 이유는 0부터 시작하기 때문

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:                                 # numRows == 1이면 한 줄이기 때문에
            return s                                     # s 그대로 반환
        answer = ''
        for num in range(numRows):                       
            add_list = collections.deque()               
            if (numRows - num - 1) != 0:                 # 첫 번째 증가 숫자가 0이 아닌 경우
                add_list.append(2*(numRows - 1 - num))   # deque에 추가
            if (2*num) != 0:                             # 두 번째 증가 숫자가 0이 아닌 경우
                add_list.append(2*num)                   # deque에 증가
            start = num
            if num > len(s) - 1:                         # 위치 숫자가 글자 길이보다 큰 경우
                break                                    # 반복문 탈출
            answer += s[start]                           # 아닌 경우, answer에 추가
            while True:                                  
                plus = add_list.popleft()                # 첫 번째 증가 숫자, 두 번째 증가 숫자를 돌아가면서 가져옴
                start += plus                            # 시작 숫자에 더함
                if start > len(s) - 1:                   # 위치 숫자가 글자 길이보다 큰 경우
                    break                                # 반복문 탈출
                answer += s[start]                       # 아닌 경우, answer에 추가
                add_list.append(plus)                    # deque에서 뽑아온 증가 숫자를 다시 deque에 추가
        return answer                                    # 결과 반환
