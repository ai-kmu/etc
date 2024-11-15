class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        new_img = list()
        for row in image:
            row = row[::-1]
            new_row = list()
            for i in row:
                if i==0: new_row.append(1)
                else: new_row.append(0)

            new_img.append(new_row)
        return new_img
