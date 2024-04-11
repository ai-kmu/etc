class Solution(object): 
    def fourSumCount(self, nums1, nums2, nums3, nums4):

        # (a+b) - (c+d)가 0이 되는 경우만 count
        var_cnt = {} 
        cnt = 0

        # (a+b)
        for a in nums1: 
            for b in nums2:  
                sum_ab = a + b

                # var_cnt에 sum_ab를 키로 가지는 값이 없으면 1로 설정하고, 있으면 1 증가시킴
                if sum_ab in var_cnt: 
                    var_cnt[sum_ab] += 1 
                else:
                    var_cnt[sum_ab] = 1
        # -(c+d)
        for c in nums3:
            for d in nums4:
                sum_cd = -(c + d) 
                # var_cnt에 sum_cd를 키로 가지는 값이 있다면
                if sum_cd in var_cnt:  
                     # cnt에 var_cnt의 sum_cd에 대응하는 값을 더함
                    cnt += var_cnt[sum_cd] 
        return cnt
