'''
아이디어
1) 무지성으로 넣기
2) 바꿀만하면 바꾸기
    - 큰 건 작은 거랑 바꾸기
    - 바꾸기: 이분탐색
'''

class Solution:    
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 바꾸기를 위한 이분 탐색
        def binsec(sub, num):
            lb = 0
            ub = len(sub) - 1
            ind = lb
            while lb <= ub:
                mid = (lb + ub) // 2
                # 같은 거 있으면 걔랑 바꿈
                if num == sub[mid]:
                    return mid

                # subsequence가 더 크면 좀 더 앞으로 가야됨
                elif num < sub[mid]:
                    ind = mid
                    ub = mid - 1

                # subsequence가 더 작으면 좀 더 뒤로 가야됨
                elif num > sub[mid]:
                    lb = mid + 1

            return ind
        
        sub = []
        for i, num in enumerate(nums):
            # subsequence가 없거나
            # 마지막 요소가 새로 들어올 애보다 작으면 그냥 추가
            if len(sub) == 0 or sub[-1] < num:
                sub.append(num)
            
            # 같으면 패스
            elif sub[-1] == num:
                continue
                            
            # 새로 들어올 애가 끝보다 더 작으면 바꾸기 위한 이분 탐색
            else:
                ind = binsec(sub, num)
                sub[ind] = num
        
        return len(sub)
                
