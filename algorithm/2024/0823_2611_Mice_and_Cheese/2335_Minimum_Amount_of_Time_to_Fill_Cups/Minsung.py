class Solution:
    def fillCups(self, amount: List[int]) -> int:
        
        amount = self.heapify(amount)
        cnt = 0
        while amount[0] > 0:
            if amount[0] > 0 and amount[1] > 0:
                amount[0] -= 1
                amount[1] -= 1
            elif amount[0] > 0:
                amount[0] -= 1
            cnt += 1
            amount = self.heapify(amount)
        return cnt

    def heapify(self, arr):
        arr.sort(key=lambda x: -x)
        return arr
