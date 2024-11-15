class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []
        
        for i in image:
            x = []
            for j in reversed(i):
                x.append(1 - j)
            ans.append(x)

        return ans

        
