class Solution:
    def maxNumber(self, nums1, nums2, k):
        def extract_max_arr(arr, size):# 배열과 추출해야하는 사이즈가 주어지면 그 사이즈에 맞게 최대값을 갖는 배열을 뽑아내줌
            i, res = 0, []
            for r in range(size - 1, -1, -1): # 차근차근 max값을 추출하면서 검사할 것

                if len(arr[i:-r]) > 0:
                    num, i = max(arr[i:-r], key=lambda item: item[0])
                else:
                    num, i = max(arr[i:], key=lambda item: item[0])
                i = i + 1
                res.append(num)

            return res
        
        def merger(arr1, arr2):# 두 배열을 조건에 맞게 합쳐주는 함수
#             print(arr1, arr2)
            res, i, j = [], 0, 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i:] >= arr2[j:]:
                    res.append(arr1[i])
                    i += 1
                else: 
                    res.append(arr2[j])
                    j += 1
            if i < len(arr1): res += arr1[i:]
            elif j < len(arr2): res += arr2[j:]
#             print(res)
#             print("=" * 10)
            return res     
        

        answer = []
        len1 = len(nums1)
        len2 = len(nums2)
        
        nums1, nums2,= [(num,i) for i, num in enumerate(nums1)], [(num,i) for i, num in enumerate(nums2)]
        for m in range(k + 1):
            if m > len(nums1) or k - m > len(nums2): continue
            arr1, arr2 = extract_max_arr(nums1, m), extract_max_arr(nums2, k - m)  
            answer.append(merger(arr1, arr2))
        return max(answer)
