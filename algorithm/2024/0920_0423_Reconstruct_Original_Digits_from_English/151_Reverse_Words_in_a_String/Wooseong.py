class Solution:
    def reverseWords(self, s: str) -> str:
        # s.split() -> words를 word로 찢음
        # [::-1] -> 순서 뒤집음
        # ' '.join() -> word를 words로 합침
        return ' '.join(s.split()[::-1])
