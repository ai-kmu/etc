class Solution:
    def isHappy(self, n: int) -> bool:
        visited = dict()
        cur = n
        while True:
            nums = [i for i in str(cur)]
            cur = 0
            for i in nums:
                cur += int(i) ** 2
            print(cur)
            try: 
                if visited[cur] == 1:
                    return False
            except:
                pass

            visited[cur] = 1

            if cur == 1:
                return True

