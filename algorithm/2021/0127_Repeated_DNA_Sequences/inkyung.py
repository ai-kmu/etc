class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # sub_string set과 answer set을 만들어서
        # sub_string에 있는 거면 정답에 추가
        sub_strings, answer = set(), set()
        for i in range(len(s) - 9):
            if s[i:i+10] in sub_strings:
                answer.add(s[i:i+10])
            sub_strings.add(s[i:i+10])
        return answer 
