class Solution:
    def simplifyPath(self, path: str) -> str:
        answer_list = list()
        answer = '/'   
        directories = path.split('/')  # /를 기준으로 나눠서 이동할 디렉토리 모두 보기
        for p in directories:
            if not p or p == '.':     # 디렉토리를 움직이지 않거나 현재에 머무를 때
                continue
            elif p == '..':     # 이전 디렉토리로 이동하는 경우
                answer_list = answer_list[:-1]      # 움직인 디레고리 중 하나 제거
            else:
                answer_list.append(p)       # 그렇지 않으면 이동한 디렉토리를 저장
        for a in answer_list:
            answer += a + '/'
        if not answer_list:
            return '/'
        return answer[:-1]
