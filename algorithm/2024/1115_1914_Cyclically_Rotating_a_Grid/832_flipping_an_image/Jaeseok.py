class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        answer = []
        for row in image:
            answer.append([1 - i for i in row[::-1]])
            
        return answer
