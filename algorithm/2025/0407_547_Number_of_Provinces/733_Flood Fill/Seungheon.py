class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        def explore(cur_i, cur_j, cur_color, object_color):

            # 예외
            if cur_i < 0 or cur_j < 0 or cur_i >= len(image) or cur_j >= len(image[0]):
                return None

            # 방문처리
            if image[cur_i][cur_j] == cur_color:
                image[cur_i][cur_j] = object_color
            else:
                return None

            for di, dj in [(0,1),(1,0),(-1,0),(0,-1)]:
                explore(cur_i+di, cur_j+dj, cur_color, object_color)

            return None

        
        cur_color = image[sr][sc]
        if cur_color == color:
            return image
        else:
            explore(sr, sc, cur_color, color)
            return image
        
