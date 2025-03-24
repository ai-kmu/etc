class Solution:
    def sumBase(self, n: int, k: int) -> int:
        target_num = n
        target_list = []
        while target_num >= k:
            target_list.append(target_num % k)
            target_num = target_num // k
        target_list.append(target_num)
        return sum(target_list)
