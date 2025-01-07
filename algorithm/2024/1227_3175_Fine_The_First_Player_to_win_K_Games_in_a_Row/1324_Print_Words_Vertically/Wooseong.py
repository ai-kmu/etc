class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")  # s를 단어로 나누기
        max_length = max(map(len, words))  # output 리스트 길이 찾기

        # 아래 과정을 하기 위해서 일단 짧은 애들은 뒤에 space 붙이기
        words = [f"{s:<{max_length}}" for s in words]
        answer = [
            "".join(w[i] for w in words).rstrip()  # 2. 각 word의 i번째 char를 합친 것
            for i in range(max_length)             # 1. i번째 string은
        ]  # 3. rstrip은 answer의 요소는 뒤에 space가 없기 때문
        return answer
