class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a = sentence1.split()
        b = sentence2.split()

        if len(a) > len(b):
            big, small = a, b
        else:
            big, small = b, a
        idx = 0
        # 앞에서부터 탐색
        while idx != len(small):
            if small[idx] != big[idx]:
                break
            idx += 1
        if idx == len(small):
            return True
        print(idx)
        # 뒤에서부터 탐색
        if small[idx-len(small):] == big[idx-len(small):]:
            return True
        return False
