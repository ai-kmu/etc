# X축이 nums를 동일하게 맞출 수이고 y축이 cost라 했을 때 함수는 아래로 볼록을 그린다.
# 따라서 아래로 볼록 함수의 최소값을 찾으면 된다.
# 최소값은 이진 탐색으로 찾는 것이 빠르다.
# 또한 이 때 최소값은 nums안의 항목들 중 하나로 정해진다.

class Solution:
    def minCost(self, nums, cost):
        nums, cost = np.array(nums), np.array(cost)
        l,r = np.min(nums), np.max(nums)
        
        while l<=r:
            m = (l+r) // 2
            
            # 아래로 볼록 함수의 최소값을 찾으려면 현재 상태에서의 기울기를 탐색하면 된다.
            # 기울기는 m+1 혹은 m-1로 찾는다.
            left_cost = np.sum(np.abs(nums - (m-1)) * cost)
            right_cost = np.sum(np.abs(nums - (m+1)) * cost)
            current_cost = np.sum(np.abs(nums - m) * cost)
            
            # 이진 탐색
            if right_cost < current_cost:
                l = m+1
            elif left_cost < current_cost:
                r = m-1
            else:
                break
                
        return current_cost
