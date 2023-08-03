# string s가 주어짐
# s를 permute해서 t라는 새로운 string을 만듦
# 자음은 유지하고 모음의 위치를 바꾸는 듯
# 모음은 sort되어야하는데, ASCII 코드의 기반으로 정렬
# 정렬하는 기준은 nondecreasing

from collections import defaultdict

vowel = 'aeiouAEIOU'


class Solution:
    def sortVowels(self, s: str) -> str:

        s = list(s)
        vowels = []
        consonants = []
        idxs = defaultdict(lambda: False)

        for idx, i in enumerate(s):
            if i in vowel:
                idxs[idx] = True
                vowels.append(i)
            else:
                consonants.append(i)
        vowels.sort(reverse = True)
        consonants = consonants[::-1]

        answer = []

        for i in range(len(s)):
            if idxs[i]:
                answer.append(vowels.pop())
            else:
                if consonants:
                    answer.append(consonants.pop())

        return ''.join(answer)
