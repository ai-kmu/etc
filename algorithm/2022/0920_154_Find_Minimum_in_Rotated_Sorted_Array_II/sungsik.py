class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        
        while l < r:
            m = (l + r) // 2
            l_num, m_num, r_num = nums[l], nums[m], nums[r]
            
            # 만약 왼쪽 값이 오른쪽 값보다 클 경우 오름차순으로 정렬되어 있으므로
            # 바로 왼쪽 값을 return
            if l_num < r_num:
                return l_num
            # 만약 중앙값이 왼쪽값이나 오른쪽값보다 클 경우
            # 최소점이 오른쪽 배열에 있다.
            elif m_num > l_num or m_num > r_num:
                l = m + 1
            # 만약 중앙값이 왼쪽값이나 오른쪽값보다 작을 경우
            # 최소점이 왼쪽 배열에 있거나 혹은 m 위치에 있다.
            elif m_num < l_num or m_num < r_num:
                r = m
            # 위의 case 모두 벗어날 경우
            # l_num == m_num == r_num의 경우에 해당된다.
            # 여기서 총 3가지의 경우의 수가 존재
            # 1. 최솟값이 왼쪽 배열에 존재할경우
            # 2. 최솟값이 오른쪽 배열에 존재할 경우
            # 3. 최솟값이 m_num일 경우
            # 3가지의 case 중 어떤 경우에 해당되는지 알려면 어차피 O(n)으로 돌아야 함으로
            # 그냥 min을 사용해서 return한다.
            else:
                return min(nums[l:r+1])
                
        return nums[l]
