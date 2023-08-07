class Solution:
    def sortVowels(self, s: str) -> str:
        # 인덱스 접근을 위해 s를 list로 바꿈
        s = list(s)
        vowels = []
        # s를 순회하면서 "aeiou"에 해당하면 vowel에 담고 위치를 대신 "0"으로 채움
        for idx, val in enumerate(s):
            if val.lower() in "aeiou":
                vowels.append(val)
                s[idx] = "0"
        # vowel의 값들을 ASCII 값을 기준으로 내림차순 정렬
        vowels.sort(key=lambda x: ord(x), reverse=True)
        # 다시 s를 순회하면서 "0"으로 대신 채워준 값들을 정렬된 vowel로 대치
        for idx, _ in enumerate(s):
            if s[idx] == "0":
                s[idx] = vowels.pop()
        # list 값을 다시 string 형태로 return
        return "".join(s)
