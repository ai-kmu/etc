class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s_list = []
        ans = ''
        
        for i in s:
            s_list.append(i)
        
        for i in range(len(s_list)):
            tmp = s_list.pop(0)
            s_list.append(tmp)
            print(s_list)
            for x in s_list:
                ans += x
            if ans == goal:
                return True
            ans = ''
        
        return False
