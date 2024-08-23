class Solution:
    def fillCups(self, amount: List[int]) -> int:
        answer = 0
        amount.sort(reverse=True)
        while amount[0] > 0:
            if amount[1] > 0:
                amount[0] -= 1
                amount[1] -= 1
                answer += 1
            else:
                amount[0] -= 1
                answer += 1
            amount.sort(reverse=True)
        return answer
      
