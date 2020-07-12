class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # nums1에서 순서대로 max인 것을 i개를 뽑고, nums2에서 k-i개를 뽑아서 그 2개를 merge함.
        # 이것을 반복하면서 최대 list를 찾음.
        if k <= 0:
            return []
        m = len(nums1)
        n = len(nums2)
        answer = [0 for _ in range(k)]
        for i in range(0, k+1):
            j = k-i
            if (i > m) or (j > n): continue
            # nums1에서 i개를 뽑음. nums1안에서 max가 되는 값들을 원래 순서대로
            sel_nums1 = self.selectMax(nums1, i)
            # nums2에서 k-i개를 뽑음. nums2안에서 max가 되는 값들을 원래 순서대로
            sel_nums2 = self.selectMax(nums2, j)
            # 큰 순서대로 merge
            merge_arr = self.mergeMax(sel_nums1, sel_nums2)
            # 기존 answer와 merge_arr를 비교하여 더 큰 숫자가 있는 것을 answer로 함.
            answer = max(merge_arr, answer)
        return answer
    # 뽑은 nums1과 nums2를 크기대로 merge
    def mergeMax(self, nums1, nums2):
        merge_arr = []
        while nums1 or nums2:
            if nums1 > nums2:
                merge_arr.append(nums1[0])
                nums1 = nums1[1:]
            else:
                merge_arr.append(nums2[0])
                nums2 = nums2[1:]
        return merge_arr
    def selectMax(self, nums, sel_num):
        '''
        nums: 뽑을 후보 list
        sel_num : 뽑아야하는 개수
        '''
        len_nums = len(nums)
        sel_indices = [-1]
        # 뽑아야하는 개수가 list의 개수보다 클 때는 패스.
        if len_nums < sel_num:
            return sel_indices
        if len_nums == sel_num:
            return nums
        # max값 앞에서부터 하나씩 선택하기
        while sel_num > 0:
            # i개를 뽑아야한다면 뒤에서부터 i-1개는 꼭 남아있어야함.
            # 마지막으로 선택한 index부터 뽑을 수 있는 구역까지 max값 탐색함.
            first_i = sel_indices[-1] + 1
            end_i = len_nums-sel_num + 1
            max_num = max(nums[first_i:end_i])
            for i in range(first_i, end_i):
                if nums[i] == max_num:
                    sel_indices.append(i)
                    break
            sel_num -= 1
        # 선택한 index의 값들로 array를 만들어 return
        sel_arr = [nums[i] for i in sel_indices[1:]]
        return sel_arr

