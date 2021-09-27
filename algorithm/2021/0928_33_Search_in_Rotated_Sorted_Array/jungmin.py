class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(lst, l, h, target): # 이진 탐색법 적용
            mid = l + (h - l)//2 # 처음 인덱스와 끝 인덱스 사이에 있는 중간 인덱스 선언
            
            if target == nums[mid]: # target이 중간 인덱스 값과 같으면 바로 정답 출력
                return mid
            
            elif l>h: # 이진 탐색을 계속하다가 target 값이 없으면 -1 리턴
                return -1
            
            # 처음 인덱스값이 중간 인덱스 값 이하인경우 해당 영역은 오름차순 정렬이 되어있으므로
            # 그 영역 안에 target이 있으면 그 영역에 다시 이진 탐색
            # 그렇지 않으면 반대쪽에 이진탐색
            if nums[l] <= nums[mid]: 
                if nums[l] <= target <= nums[mid]:
                    return bs(nums, l, mid-1, target)
                else:
                    return bs(nums, mid+1,h, target)
            # 처음 인덱스값이 중간 인덱스 값 초과인경우
            # 중간 인덱스의 값부터 끝 인덱스까지 영역에 이진 탐색 적용하여
            # 그 영역에 target이 있으면 그 영역에 이진탐색
            # 그렇지 않으면 반대쪽에 이진 탐색
            else:
                if nums[mid] <= target <= nums[h]:
                    return bs(nums, mid+1, h, target)
                else:
                    return bs(nums, l, mid-1, target)
                
        return bs(nums, 0, len(nums)-1, target)
        
