class Solution:
    def sortVowels(self, s: str) -> str:
        vs = set(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'])
        vl = []
        indices = []

        for idx, letter in enumerate(s):
            if letter in vs:
                indices.append(idx)
                vl.append(letter)

        vl.sort(key=lambda x: -ord(x))
        s = list(s)

        for idx in indices:
            s[idx] = vl.pop()

        return ''.join(s)
