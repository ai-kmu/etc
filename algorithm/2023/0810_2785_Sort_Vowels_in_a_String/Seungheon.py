class Solution(object):
    def sortVowels(self, s):

        # list 만들기
        s = list(s)
        # vowels
        vowels_list = ['a','e','i','o','u','A','E','I','O','U']

        # vowels 저장
        vowels = []
        # vowels index저장
        s_idx = []
        
        for i, c in enumerate(s):
            if c in vowels_list:
                vowels.append(c)
                s_idx.append(i)

        vowels.sort()

        for i, c_i in enumerate(s_idx):
            s[c_i] = vowels[i]

        return ''.join(s)
