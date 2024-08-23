import heapq

class Solution:

    def is_able_to_remove_two(self, input_list):
        removed_idx = [0, 0, 0]
        able_to_remove_cnt = 0
        for idx in range(3):
            if input_list[idx] > 0 and able_to_remove_cnt < 2:
                able_to_remove_cnt += 1
                removed_idx[idx] += 1
        if able_to_remove_cnt == 2:
            return True, removed_idx
        else:
            return False, removed_idx
            
    def fillCups(self, amount: List[int]) -> int:

        #heapq.heapify(amount)

        amount.sort(reverse=True)
        left_amount = amount
        cnt = 0

        while True:
            left_amount.sort(reverse=True)
            is_able_to_remove, removing_idx = self.is_able_to_remove_two(left_amount)
            if is_able_to_remove:
                for idx in range(3):
                    left_amount[idx] = left_amount[idx] - removing_idx[idx]
            else:
                is_found = False
                for idx in range(3):
                    if left_amount[idx] > 0:
                        left_amount[idx] = left_amount[idx] - 1
                        is_found = True
                    
                if is_found is not True:
                    break
            print(left_amount)
            cnt += 1
        return cnt
            

