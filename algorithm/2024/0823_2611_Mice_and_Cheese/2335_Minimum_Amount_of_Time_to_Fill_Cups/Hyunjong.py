# 다른 타입의 물 2개, or 같은 타입의 물 1개
# cold warm hot 순으로 분배
class Solution(object):
    def fillCups(self, amount):
        amount.sort(reverse=True)
        count = 0
        iter_num = (amount[0] + amount[1] + amount[2])
        for i in range(iter_num):
            if amount[0] != 0 and amount[1] != 0:
                amount[0] -= 1
                amount[1] -= 1
                count += 1
                amount.sort(reverse=True)
            elif amount[0] != 0 and amount[1] == 0:
                amount[0] -= 1
                count += 1
                amount.sort(reverse=True)
            else:
                break
        return count
