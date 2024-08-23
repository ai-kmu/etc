class Solution:
    def fillCups(self, amount: List[int]) -> int:
        answer = 0
        while amount != [0, 0, 0]:
            answer += 1
            amount = sorted(amount, reverse=True)
            amount[0] = amount[0] - 1
            amount[1] = amount[1] - 1
            if amount[0] == -1:
                amount[0] += 1
            if amount[1] == -1:
                amount[1] += 1
        
        return answer

