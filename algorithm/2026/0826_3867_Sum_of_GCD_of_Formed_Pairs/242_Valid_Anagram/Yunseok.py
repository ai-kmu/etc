class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        list_s = [0 for i in range(60)]
        for ch in s:
            idx = ord(ch) - ord('A')
            list_s[idx] += 1
            

        list_t = [0 for j in range(60)]
        for ch in t:
            idx = ord(ch) - ord('A')
            list_t[idx] += 1

        for idx in range(60):
            if list_s[idx] != list_t[idx]:
                return False
            print(list_s[idx], list_t[idx])

        print(list_s)
        print(list_t)

        return True
