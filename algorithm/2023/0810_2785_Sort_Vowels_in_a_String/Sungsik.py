class Solution:
    def sortVowels(self, s: str) -> str:
        VOWEL = {"A", "E", "I", "O", "U", 'a', 'e', 'i', 'o', 'u'}
        
        indices = set()
        vowels = []
        
        # 모음과 그 index들을 추가
        for i, c in enumerate(s):
            if c in VOWEL:
                indices.add(i)
                vowels.append(c)
        
        # 정렬
        vowels.sort(reverse=True)
        
        # 모음 index에 해당하는 값들을 정렬된 모음으로 변경
        # 만약 s = s[:i] + vowels.pop() + s[i+1:] 과 같이 변경하게 되면 시간이 오래 걸려서
        # answer라는 새로운 string에 추가하는 것으로 구현
        answer = ""
        for i in range(len(s)):
            if i in indices:
                answer += vowels.pop()
            else:
                answer += s[i]
        
        return answer
        
