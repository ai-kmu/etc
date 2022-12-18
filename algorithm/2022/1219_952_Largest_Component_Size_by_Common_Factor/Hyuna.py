
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:

        def union(a, b):
            a = find(a)
            b = find(b)
            if (a != b):
                self.parent[a] = b
        
        def find(a):
            if a not in self.parent:
                self.parent[a] = a

            if self.parent[a] != a:
                self.parent[a] = find(self.parent[a])

            return self.parent[a]

        self.parent = {}
        for num in nums:
            for i in range(2, int(math.sqrt(num)+1)):
                # 약수일 때 부모 연결 
                if num % i == 0:
                    union(num, i)
                    union(num, num // i)
        
        ans = 0
        cnt = {}
        # 가장 큰 연결 찾기 
        for num in nums:
            parent = find(num)
            if parent not in cnt:
                cnt[parent] = 1
            else:
                cnt[parent] += 1
            ans = max(ans, cnt[parent])

        return ans
