class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []
        for img in image:
            img.reverse()
            ans.append([x ^ 1 for x in img])
        return ans
