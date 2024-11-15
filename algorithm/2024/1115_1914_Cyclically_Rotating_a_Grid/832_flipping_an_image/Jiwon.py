class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        img_len = len(image)
        for i in range(img_len):
            image[i].reverse()
            for j in range(img_len):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image
                
