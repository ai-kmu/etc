# 풀이 실패
# 문제 이해를 잘못 해서 배열 안에 있는 숫자로 같아야 하는 것으로 착각함

#오류 코드

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        list_ = list(zip(nums, cost))
        n = len(list_)
        list_.sort(key=lambda x:x[0])

        l = 0
        r = n
        if n == 2:
            return abs(nums[0] - nums[1]) * min(cost)

        while l <= r:
            m = (l + r) // 2
            print(m)
            l_cost, m_cost, r_cost = 0, 0, 0
            for i in range(n):
                l_cost += abs(list_[i][0] - list_[m-1][0]) * list_[i][1]
                m_cost += abs(list_[i][0] - list_[m][0]) * list_[i][1]
                r_cost += abs(list_[i][0] - list_[m+1][0]) * list_[i][1]

            if l_cost < m_cost:
                r = m - 1
            elif r_cost < m_cost:
                l = m + 1
            else:
                break

        return m_cost

            
# 다른 사람 풀이 참고해서 만든 정답 코드
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # 목표하는 수는 최솟값과 최댓값 사이에 있으므로 사이를 탐색
        l = min(nums)
        r = max(nums)

        while l <= r:
            # 중간값 m을 설정
            m = (l + r) // 2
            # 중간갑과 중간값 바로 왼쪽의 값과 중간값과 중간값 바로 오른쪽의 값의 cost를 계산
            l_cost, m_cost, r_cost = 0, 0, 0
            # 이 때 두 값 사이의 차이이므로 절댓값을 구한 다음에 cost를 곱함
            for n, c in zip(nums, cost):
                l_cost += abs(n - (m - 1)) * c
                m_cost += abs(n - m) * c
                r_cost += abs(n - (m + 1)) * c

            # 만약에 중간 cost보다 왼쪽의 cost가 낮다면 왼쪽을 탐색
            if l_cost < m_cost:
                r = m - 1
            # 만약에 중간 cost보다 오른쪽의 cost가 낮다면 오른쪽을 탐색
            elif r_cost < m_cost:
                l = m + 1
            # 둘 다 아니라면 중간값의 cost가 가장 낮은 것이 되므로 종료
            else:
                break

        return m_cost
