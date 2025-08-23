# 못 풀었습니다. 풀이 안해주셔도 됩니다..
# 테케는 맞는데 흠...

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # p1, p2를 지나는 직선의 방정식
        def line_func(p1, p2):
            if p1[0] == p2[0]:
                return lambda p: p[0] - p1[0]

            elif p1[1] == p2[1]:
                return lambda p: p[1] - p1[1]
            
            else:
                return lambda p: ((p2[1] - p1[1]) / (p2[0] - p1[0])) * (p[0] - p1[0]) - (p[1] - p1[1])

        # x, y축별 max min
        x_axis = [max(trees, key=lambda x:x[0]), max(trees, key=lambda x:-x[0])]
        y_axis = [max(trees, key=lambda x:x[1]), max(trees, key=lambda x:-x[1])]

        # x, y축별 max min값을 잇는 테두리 방정식 정의
        line_list_func = lambda p: line_func(x_axis[0], y_axis[0])(p) * line_func(x_axis[0], y_axis[1])(p) * line_func(x_axis[1], y_axis[0])(p) * line_func(x_axis[1], y_axis[1])(p)

        ret = []
        
        # 하나라도 포함되면 추가
        # print(x_axis)
        # print(y_axis)
        for tree in trees:
            # print(f"{tree} :", [line_func(x_axis[0], y_axis[0])(tree), line_func(x_axis[0], y_axis[1])(tree), line_func(x_axis[1], y_axis[0])(tree), line_func(x_axis[1], y_axis[1])(tree)])
            if line_list_func(tree):
                continue

            ret.append(tree)

        return ret
