class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 홀수가 k개가 포함되는 window개수를 return

        # two pointer
        odd_indice = [0] # 왼쪽 끝점
        for i, v in enumerate(nums):
            if v % 2 == 1:
                odd_indice.append(i+1)
        odd_indice.append(len(nums)+1) # 오른쪽 끝점

        if k > len(odd_indice)-2:
            return 0

        answer = 0

        left_point = 1
        right_point = k
        
        while right_point + 1 < len(odd_indice):
            left_gap = odd_indice[left_point] - odd_indice[left_point-1]
            right_gap = odd_indice[right_point+1] - odd_indice[right_point]
            answer += left_gap * right_gap
            
            left_point += 1
            right_point += 1

        return answer
