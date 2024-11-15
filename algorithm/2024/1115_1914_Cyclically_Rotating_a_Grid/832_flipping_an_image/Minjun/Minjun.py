class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        for l in image:
            tmp = []
            for i in range(len(l)):
                k = l.pop()
                if k == 1:
                    tmp.append(0)
                else:
                    tmp.append(1)
            result.append(tmp)
        return result
                
