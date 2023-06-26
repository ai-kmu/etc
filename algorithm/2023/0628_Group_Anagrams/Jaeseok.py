# time limit exceed

from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = [[strs.pop(0)]]
        for i in strs:
            for j in anagrams:
                # 매 아나그램을 순회하면서 모든 str의 문자를 세야 하므로 매우 느림
                if Counter(j[0]) == Counter(i):
                    j.append(i)
                    break
            else:
                anagrams.append([i])
        return anagrams


# defauldict 사용
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # list를 value로 받는 defaultdit 선언
        answer = defaultdict(list)
        # str를 순회함
        for i in strs:
            # letter를 정렬하고 다시 str 형태로 만들어 같은 아나그램은 같은 문자가 되도록 함
            letters = "".join(sorted(i))
            answer[letters].append(i)

        # answer가 딕셔너리이므로 value 값들을 list 형태로 반환    
        return list(answer.values())
