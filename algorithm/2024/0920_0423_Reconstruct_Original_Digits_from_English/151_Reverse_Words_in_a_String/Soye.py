class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        
        ans = ''
        for i in range(len(arr), 0, -1):
            ans += arr[i-1]
            if i != 1:
                ans += ' '

        return ans    
