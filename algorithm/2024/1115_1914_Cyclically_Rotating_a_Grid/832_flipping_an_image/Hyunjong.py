class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        reverse_image = []
        for i in range(len(image)):
            reverse_image.append(list(reversed(image[i])))
        
        for i in range(len(reverse_image)):
            for j in range(len(reverse_image[i])):
                if reverse_image[i][j] == 0:
                    reverse_image[i][j] = 1
                else:
                    reverse_image[i][j] = 0
        return reverse_image
