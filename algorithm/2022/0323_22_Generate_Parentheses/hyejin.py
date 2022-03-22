class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        
        # 안좋은 방법
        # n으로 만들 수 있는 모든 pair를 만든 뒤에, 그 string이 유효한지 검사하는 방법
        
        # 재귀 함수
        def recursive(curr_s, num_of_front, num_of_back):
            if num_of_front == n and num_of_back == n: # (과 )의 개수가 꽉찼을 떄
                return answer.append(curr_s)
            else:
                if num_of_front < n: # "("를 추가할 때는 n개에 도달할 때까지
                    recursive(curr_s + "(", num_of_front + 1, num_of_back)
                if num_of_front > num_of_back: # ")"를 추가할 때는 "("가 있을 때
                    recursive(curr_s + ")", num_of_front, num_of_back + 1)
        recursive("", 0, 0)
        
        return answer
