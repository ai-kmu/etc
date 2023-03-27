class Solution(object):
    def kthSmallest(self, matrix, k):
        # list 더하고 sort해서 풀기
        n = len(matrix)
        list_sort = []
        for i in range(n):
            list_sort = list_sort + matrix[i]
        return(sorted(list_sort)[k-1])
