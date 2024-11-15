class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(image[0])

#         print(image)
        for i in range(len(image)):
            image[i].reverse()
            for j in range(n):
                if image[i][j] == 1:
                    image[i][j] = 0
                else:
                    image[i][j] = 1
        return image
