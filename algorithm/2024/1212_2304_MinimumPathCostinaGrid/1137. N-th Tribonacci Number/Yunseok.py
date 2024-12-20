class Solution:

    def recur(self, n, tri_list):
        if tri_list[n] != -1:
            return tri_list[n]
        else:
            if n <= 0:
                return 0
            elif n == 1:
                return 1
            elif n == 2:
                return 1

            tri_list[n] = self.recur(n - 3, tri_list) + self.recur(n - 2, tri_list) + self.recur(n - 1, tri_list)
            return tri_list[n]

    def tribonacci(self, n: int) -> int:
        tri_list = [-1] * 38
        tri_list[0] = 0
        tri_list[1] = 1
        tri_list[2] = 1

        return self.recur(n, tri_list)



        
