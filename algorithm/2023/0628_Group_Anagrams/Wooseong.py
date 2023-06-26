from collections import defaultdict as ddict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 단어들을 사전순으로 anagram 만들어두기
        sorted_s = [''.join(sorted(s)) for s in strs]
        
        # 해당 anagram을 만들 수 있는 단어들을 리스트로 갖는 ddict 정의하기
        answer = ddict(list)
        for i, s in enumerate(sorted_s):
            answer[s].append(strs[i])
        
        # 답은 ddict의 value
        return list(answer.values())
