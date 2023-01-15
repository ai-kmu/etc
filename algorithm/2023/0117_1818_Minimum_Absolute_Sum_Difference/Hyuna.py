from bisect import bisect_left

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        
        total = 0
        diff = []
        ans = float('inf')

        # for문을 돌며 absolute sum difference를 구해서 total에 더해줌 
        # 각각의 absolute sum difference는 이후에 연산을 위해 diff에 저장해줌 
        for num1, num2 in zip(nums1, nums2):

            temp = abs(num1 - num2)
            total += temp
            diff.append(temp)

        # total이 0이라면 더이상 계산해줄 필요가 없음 
        if not total:
            return total
        # total이 0이 아닐 경우
        else:
            # 각 nums2의 값을 nums1에 있는 가장 가까운 값을 찾아 변경하며 해당 차례의 diff값보다 작아지는지 확인함 
            # 바이너리 서치를 위해 정렬 필요
            nums1.sort()
            # dif는 num2에 해당하는 absolute sum difference
            for num2, dif in zip(nums2, diff):
                # 바이너리 서치를 통해 num2이 nums1의 어느 위치에 들어갈 수 있는지 인덱스를 찾아줌 
                index = bisect_left(nums1, num2)
                # index가 0과 nums1길이 사이라면 인덱스 앞뒤를 모두 보고 더 작은 값을 저장해줌 
                if index != 0 and index != len(nums1):
                    tempabs = min(abs(nums1[index-1] - num2), abs(nums1[index] - num2))
                # 인덱스가 0이라면 전 인덱스는 안봄 
                elif index == 0:
                    tempabs = abs(nums1[index] - num2)
                # 인덱스가 길이와 같을 경우 전 인덱스만 확인 
                else:
                    tempabs = abs(nums1[index-1] - num2)
                # 새로운 absolute sum difference가 기존의 absolute sum difference보다 작다면 
                # 기존에 저장하고 있던 정답값과 전체에서 기존 차액을 빼고 새로운 차액을 넣어준 값과 비교하여 더 작은 값을 저장해둠  
                if dif > tempabs:
                    ans = min(ans, total - dif + tempabs)

        return ans % (pow(10, 9) + 7)
