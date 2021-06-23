class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        lim = a+b+max(max(forbidden) , x)#조건이 확실하지 않음
        queue  = [(x , 0 , False )]
        while queue:
            curr , jump , is_back = queue.pop(0)
            if curr ==0:
                return jump
            if (curr < 0 or curr > lim) or curr in forbidden:
                continue
            forbidden.add(curr)
            if not is_back:
                queue.append((curr+b , jump+1 , True))
            queue.append((curr-a  , jump+1 , False))
        return -1
