# Wrong Answer 60 / 763 testcases passed

class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        time = 0
        energy = 0
        x = 1
        updated_x = 1

        break_idx = 0

        if len(strength) == 1:
            return strength[0]

        def get_max(curr_energy, num_list):
            max_num = 0
            
            for i in num_list:
                if i <= curr_energy:
                    max_num = max(max_num, i)
            
            return max_num

        # energy보다 작은 가장 큰 수를 먼저 제거?
        while break_idx < len(strength):
            max_num = get_max(energy, strength)
            # print(max_num)
            if max_num != 0 and max_num <= energy:
                break_idx += 1
                updated_x += k
                x += energy

            energy += x 
            time += 1
            
            # print(time, energy, x, updated_x)

        return time
