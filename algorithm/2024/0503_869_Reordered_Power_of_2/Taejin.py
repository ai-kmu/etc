from collections import defaultdict

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # 자릿수에 맞는 정렬된 숫자와 비교
        bin_dict = defaultdict(bool)
        i = 1
        while len(str(i)) <= len(str(n)):
            bin_dict["".join(sorted(str(i)))] = True
            i *= 2

        return bin_dict["".join(sorted(str(n)))]
