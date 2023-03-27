class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        sorted_matrix = []
        # matrix를 풀어서 list에 저장
        for mat in matrix:
            for num in mat:
                sorted_matrix.append(num)
        # 저장한 list를 정렬한 뒤 인덱스에 맞춰서 return
        return sorted(sorted_matrix)[k-1]
        
