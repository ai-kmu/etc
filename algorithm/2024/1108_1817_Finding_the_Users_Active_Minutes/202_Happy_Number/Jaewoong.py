class Solution:
    def isHappy(self, n: int) -> bool:
        num_list = []
        for i in str(n):
            num_list.append(i)
        add_num = 0 
        add_list = []
        x = 0
        while True:
            for n in num_list:
                add_num += int(n) * int(n)
            num_list = []
                
            if add_num == 1:
                return True
                break

            for a in str(add_num):
                num_list.append(a)

            add_num = 0
            
            x += 1
            if x == 10000:
                return False
                break
