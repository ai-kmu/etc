class Solution:
    def minAbsoluteSumDiff(self, nums1:List[int], nums2:List[int]) -> int:
        n =len(nums1)
        differences = [] # 같은 인덱스끼리 절대 차를 저장하는 리스트
        absolute_sum_difference = 0 # 입력에서 총 절대차들의 합
        for i in range(n):
            difference = abs(nums1[i] - nums2[i])
            differences.append(difference)
            absolute_sum_difference += abs(nums1[i] - nums2[i])

        best_difference = []
        nums1.sort() # 이진 탐색을 위해 nums1 정렬
        
        '''
        nums2를 for문 돌면서 nums1을 이진 탐색(왼쪽)한 인덱스(ind)를 구한 후
        nums1[ind]와 nums2[i]간의 절대차를 best_difference에 저장
        ind가 0이거나 n인 경우 nums1의 양 끝과만 절대차를 구하고
        그 외의 ind가 나오는 경우 두 가지의 차이를 구할 수 있으므로 그 두 가지중 작은 것을 
        best_difference에 저장.
        결국 best_difference는 nums2[i]가 nums1의 요소들이랑 차를 각각 구할 때 그 중 가장 작은 값을
        저장하는 리스트
        '''
        for i in range(n):
            ind = bisect.bisect_left(nums1, nums2[i])
            if ind != 0 and ind != n:
                best_difference.append(min(abs(nums1[ind]-nums2[i]), abs(nums1[ind-1]-nums2[i])))
            elif ind == 0:
                best_difference.append(abs(nums1[ind]-nums2[i]))
            else:
                best_difference.append(abs(nums1[ind-1]-nums2[i]))

        final_diffs = [] # 인덱스별로 differences과 best_difference의 차이를 저장
        for i in range(n):
            final_diffs.append(differences[i] - best_difference[i])
        # absolute_sum_difference에서 final_diff의 요소들 중 가장 큰 값을 빼서 최종 답 구함
        ans = absolute_sum_difference - (final_diffs[final_diffs.index(max(final_diffs))])
         
        # 문제에서 최종 답이 큰 것을 대비해 (10**9)+(7)의 나머지를 연산하라 했으므로 정답에서 나머지 연산 후 리턴
        return ans % ((10**9)+(7))
        
        
