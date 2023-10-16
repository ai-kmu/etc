class Solution(object):
    def isPossibleDivide(self, nums, k):
        from collections import Counter
        count_map = Counter(nums)
        
        # 숫자를 오름차순으로 정렬
        for num in sorted(count_map.keys()):
            # 이미 사용된 숫자라면 건너뛴다 (빈도가 0 이하)
            if count_map[num] <= 0:
                continue
            
            # 현재 숫자로부터 k만큼 큰 숫자의 빈도를 감소시키고, 음수가 되면 False를 반환
            for index in range(1, k):
                count_map[num + index] -= count_map[num]
                if count_map[num + index] < 0:
                    return False
        
        # 모든 숫자를 반복하고도 조건을 만족하면 True를 반환
        return True
