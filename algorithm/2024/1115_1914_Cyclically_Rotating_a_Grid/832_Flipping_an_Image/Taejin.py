class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[int(not j) for j in i][::-1] for i in image]
