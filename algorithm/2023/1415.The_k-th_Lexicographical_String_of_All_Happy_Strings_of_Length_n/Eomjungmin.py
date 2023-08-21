class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # strings: 문제 조건에 부합한 string을 저장하는 리스트 선언
        strings = []

        # 재귀적인 방법 사용
        def search_string(string):
            # 입력 string의 길이가 n이랑 같으면 strings에 추가
            if len(string) == n:
                strings.append(string)
                return

            """
            입력 string의 마지막 철자와 같지 않은 것만
            알파벳 추가하여 backtracking 함수에 다시 입력
            """
            for i, c in enumerate(["a", "b", "c"]):
                if string[-1] == c:
                    continue
                search_string(string + c)

        # 시작이 'a','b','c'일 때 search_string 함수를 통해 모든 string 구함
        for s in ["a", "b", "c"]:
            search_string(s)
        
        if len(strings) < k:
            return ""
        else:
            return strings[k - 1]
