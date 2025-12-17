class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heapify(heap:=[(-a, 'a'), (-b, 'b'), (-c, 'c')])
        n, ch = heappop(heap)
        ans = []
        while n:
            if n == -1 or heap[0][0] < n:
                ans.append(ch)
                n += 1
            else:
                ans.append(ch*2)
                n += 2
            n, ch = heapreplace(heap, (n, ch))
        return ''.join(ans)
