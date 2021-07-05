class Solution:
    def minimumJumps(self, forbidden, a, b, x):

        box = [(0, True)]

        max_N = x+b 
        if a < b:
            max_N = max(x, max(forbidden))
            max_N +=2 * a + b
        
        dp_table = set()      
        dp_table.add((0, True))
        for i in forbidden:
            dp_table = dp_table | set([(i, True), (i,False)])
        
        
        ans = 0
        while box:
            new_box = []
            
            for i, back in box:
                if i == x:
                    return ans
                
                if i+a <= max_N and (i+a, True) not in dp_table:
                    new_box.append((i+a, True))
                    dp_table.add((i+a, True))
                
                if i-b >= 0 and (i-b, False) not in dp_table and back:
                    new_box.append((i-b, False))
                    dp_table.add((i-b, False))

            box = new_box
            ans += 1

        return -1
    
