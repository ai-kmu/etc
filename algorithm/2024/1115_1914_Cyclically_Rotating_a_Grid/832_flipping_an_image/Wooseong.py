class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        answer = []
        for row in image:
            # 1 - r은 invert, row[::-1]은 flip
            answer.append([(1 - r) for r in row[::-1]])
        return answer
