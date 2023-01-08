class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:

        # y값을 기준으로 오름차순, y값이 같으면 x값을 기준으로 오름차순 정렬
        rectangles.sort(key = lambda x :(x[1], x[0]))

        # 왼쪽 아래부터 쌓는 방식으로 rectangles을 만드는지 확인한다.

        # 시작부분 찾기
        min_height = float('inf')
        max_width = float('-inf')
        min_width = float('inf')
        for x, y, a, b in rectangles:
            x += 10**5
            a += 10**5
            min_width = min(x, min_width)
            max_width = max(a, max_width)
            min_height = min(y, min_height)

        # 쌓을 list 만들기
        heights = [ min_height for i in range(max_width+1)]

        # 이어지게 쌓으면 계속 쌓고 이어지지 않으면 False return
        for x, y, a, b in rectangles:
            x += 10**5
            a += 10**5
            for i in range(x, a):
                i += 1
                if heights[i] == y:
                    heights[i] = b
                else:
                    return False

        # 모두 같은 높이로 채웠으면 True 아니면 False
        if all(heights[-1] == i for i in heights[min_width+1:]):
            return True
        else:
            return False
