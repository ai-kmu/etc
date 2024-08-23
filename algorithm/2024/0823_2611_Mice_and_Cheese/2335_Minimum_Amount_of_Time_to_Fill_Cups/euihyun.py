class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        
        cold, warm, hot = amount[0], amount[1], amount[2]
        cnt = 0
        for i in range(100000):
            if not amount :
                break
            max_num = max(amount)
            min_num = min(amount)
            if max_num != 0 and min_num != 0 and len(amount) != 1:
                amount[amount.index(max_num)] = max(amount) - 1
                amount[amount.index(min_num)] = min(amount) - 1
                cnt += 1
                print(amount)

            elif min_num == 0:
                del(amount[amount.index(min_num)])
#                 print(amount, 'amount')
#                 print(len(amount),'len')
            elif len(amount) == 1:
            
                amount[0] -= 1
                print(amount)
                cnt += 1
            elif max_num != 0 and min_num == 0:
                amount[amount.index(max_num)] = max(amount) - 1
                cnt += 1

                
        return cnt
        
