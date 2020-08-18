class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:   # 전체가 회문일 경우는 그대로 리턴
            return s
        sample = set()
        for i in range(len(s)):
            lst1 = list()
            for k in range(i, len(s)):   # 회문이 있는지 찾기
                lst1.append(s[i: k+1])
            for w in lst1:
                if w == w[::-1]:  # 회문일 경우 set에 저장
                    sample.add(w)
        sample = list(sample)
        max_length, idx = len(sample[0]), 0
        for i in range(1, len(sample)):   # 길이가 가장 긴 회문 찾기
            if len(sample[i]) > max_length:
                max_length = len(sample[i])
                idx = i
        return sample[idx]
