class Solution:
    def sortVowels(self, s: str) -> str:
        indices = []
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i, _ in enumerate(s):
            if _.lower() in vowels:
                indices.append(i)
        v = []
        for _ in indices:
            v.append(s[_])
        v.sort()
        ans = [*s]
        if indices:
            for i, k in enumerate(v):
                ans[indices[i]] = v
        print(''.join(ans))
