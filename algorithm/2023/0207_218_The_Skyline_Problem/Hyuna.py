class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        # 0 <= lefti < righti <= 231 - 1 해당 조건 고려 못해서 실패 
        arr = [0] * 10000000
        h = 0
        ans = []

        for start, end, height in buildings:
            building = arr[start:end]
            for i in range(len(building)):
                if building[i] < height:
                    arr[start+i] = height

                
        for i in range(len(arr)):
            if h != arr[i]:
                h = arr[i]
                ans.append([i, h])
        
        if ans[-1][1] != 0:
            ans.append([h, 0])
        
        return ans
            
            
