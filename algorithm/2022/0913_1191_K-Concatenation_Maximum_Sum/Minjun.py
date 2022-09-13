class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        '''
        모든 sub-sequence의 합을 구한다 -> tmp_sum
        최대값을 유지한다 -> max_sum
        k < 3, return max_sum
        k >= 3, return arr 합 or arr*2 합( 2개 이어붙인 배열 중간 값이 최대인 경우, 이 경우 sum(arr)이 음수다.) or sum(arr)*(k-2) + 배열 좌,우 합 ex)[a[i:]+sum(arr)+a[:j]]   
        '''
        def makeSum(arr):
            tmp_sum = arr[0]
            max_sum = arr[0]
            for i in range(1,len(arr)):
                tmp_sum = max(arr[i], tmp_sum+arr[i])
                if tmp_sum < 0:
                    tmp_sum = 0
                max_sum = max(max_sum, tmp_sum)
                
            return max_sum
        
        if k < 3:
            return makeSum(arr*k)%(10**9+7)
        
        return max([makeSum(arr), makeSum(arr*2), makeSum(arr*2) + sum(arr)*(k-2)])%(10**9+7)
