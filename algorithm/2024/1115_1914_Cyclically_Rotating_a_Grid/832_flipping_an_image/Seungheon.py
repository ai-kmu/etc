class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for i, raw in enumerate(image):
            new_raw = [ 0 if x==1 else 1 for x in raw[::-1]]
            image[i] = new_raw
        
        return image
