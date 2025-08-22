# 풀이 실패
class Solution(object):
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cal_direct(a, b, c):
            return (c[1] - b[1]) * (b[0] - a[0]) - (b[1] - a[1]) * (c[0] - b[0])
        
        def updateEdges(tree):
            while len(upper_edges) >= 2 and cal_direct(upper_edges[-2], upper_edges[-1], tree) < 0:
                upper_edges.pop()
            while len(lower_edges) >= 2 and cal_direct(lower_edges[-2], lower_edges[-1], tree) > 0:
                lower_edges.pop()
                
        trees.sort()
        upper_edges = []
        lower_edges = []
        
        for tree in trees:
            updateEdges(tree)
            upper_edges.append(tuple(tree))
            lower_edges.append(tuple(tree))
        
        return set(upper_edges + lower_edges)
