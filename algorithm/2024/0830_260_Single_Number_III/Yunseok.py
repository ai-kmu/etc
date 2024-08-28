class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 리스트를 오름차순으로 정렬
        nums.sort()
        
        num_len = len(nums)
        idx = 0
        
        # 한 번만 등장한 숫자들을 저장할 리스트
        once_appeared_list = []
        
        # 리스트를 순회하면서, 한 번만 등장한 숫자 찾음
        while idx < num_len:
            current_elem = nums[idx]
            # 현재 원소와 그 다음 원소가 같은 경우, 두 개를 건너뜀
            if idx < num_len - 1 and current_elem == nums[idx + 1]:
                idx += 2
            else:
                # 한 번만 등장한 경우 리스트에 추가하고 인덱스를 1 증가
                once_appeared_list.append(current_elem)
                idx += 1
        
        return once_appeared_list
