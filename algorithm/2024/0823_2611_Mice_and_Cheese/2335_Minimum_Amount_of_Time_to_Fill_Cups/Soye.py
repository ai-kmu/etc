class Solution:
    def fillCups(self, amount: List[int]) -> int:
        cnt = 0
        while True:
            sum_ = sum(amount)
            if sum_  == 0:
                break
            amount.sort(reverse=True)
            amount[0] = amount[0]-1
            if amount[1] != 0:
                amount[1] = amount[1]-1
            cnt = cnt + 1

        return cnt



        
