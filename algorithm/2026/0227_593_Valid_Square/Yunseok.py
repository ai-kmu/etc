class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
      
        def get_dist_sq(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        
        distances = [
            get_dist_sq(p1, p2),
            get_dist_sq(p1, p3),
            get_dist_sq(p1, p4),
            get_dist_sq(p2, p3),
            get_dist_sq(p2, p4),
            get_dist_sq(p3, p4)
        ]
        
        unique_distances = set(distances)
        return 0 not in unique_distances and len(unique_distances) == 2
