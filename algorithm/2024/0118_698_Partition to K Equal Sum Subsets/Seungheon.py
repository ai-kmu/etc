# failcode 
# dp로풀려고 했는데 싪패

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        nums.sort()

        if sum(nums)%k != 0:
            return False
        
        object_num = sum(nums)/k

        def explore(obj_num, num_list):
            print(obj_num)
            print(num_list)

            if not num_list:
                return True 

            new_num_list = []
            new_object_list = []
            flag_Set = set()
            for num in num_list:
                new_num = obj_num - num
                if new_num < 0:
                    return False
                elif new_num == 0:
                    if num in flag_Set:
                        new_num_list.append(num)
                        new_object_list.append(new_num)
                    else:
                        flag_Set.add(num)
                        continue
                else:
                    new_num_list.append(num)
                    new_object_list.append(new_num)

            for new_object_num in new_object_list:
                if not explore(new_object_num, new_num_list):
                    continue
                else:
                    return True

            return False

        return explore(object_num, nums)
