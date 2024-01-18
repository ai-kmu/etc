class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        a = []
        def recursion(num):
            if len(num) == n:
                print('hi')
                a.append(int(num))
                return
            for i in range(0,10):
                if abs(int(num[-1]) - i) == k:
                    print('find', num+str(i))
                    recursion(num+str(i))
        for i in range(1,10):
            recursion(str(i))
        return a
