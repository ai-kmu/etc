# 풀이실패 어케푸노
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        target = sorted(arr)
        ans = []
        i = 0
        while arr:
            i += 1
            a = arr.index(min(arr))
            ans.append(a)
            #tmp = list(reversed(arr[:a]))
            del arr[a]
            #arr = list(reversed(arr[:a])) + arr[i:]

        return ans


    
