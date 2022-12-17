from collections import defaultdict as ddict

class Solution:
    '''
    알고리즘 예시 (60 ~ 72번째 주석 대체)
    [4, 6, 15, 35]의 경우
    1. p = 2
      1. 4를 prev로 지정
      2. 6이 다음으로 걸림 -> union(4, 6) -> prt, qrt = 4, 6
         둘 다 size가 1이므로 parent[6]이 4로 변경, size[4] 1 증가 (2)
    2. p = 3
      1. 6을 prev로 지정
      2. 15가 다음으로 걸림 -> union(6, 15) -> prt, qrt = 4, 15
         size[4]가 커서 변경 x, parent[15]가 4로 변경, size[4] 1 증가 (3)
    3. p = 5
      1. 15를 prev로 지정
      2. 35가 다음으로 걸림 -> union(15, 35) -> prt, qrt = 4, 35
         size[4]가 커서 변경 x, parent[35]가 4로 변경, size[4] 1 증가 (4)
    4. p = 7 ~ 35: 32번째 줄을 거쳐 아무 일도 일어나지 않음
    '''
    def largestComponentSize(self, nums: List[int]) -> int:
        # union find
        def find(p):
            if p != parent[p]:
                parent[p] = find(parent[p])
            return parent[p]
        
        def union(p, q):
            prt = find(p)
            qrt = find(q)
            if prt == qrt:
                return
            if size[prt] < size[qrt]:
                prt, qrt = qrt, prt
            parent[qrt] = prt
            size[prt] += size[qrt]


        '''
        변수들
            n       : nums의 최댓값 - 여기까지 처리해야함
            given   : 탐색을 O(1)로 하기 위해 nums를 set으로 변경
            parent  : union find를 위해 1 ~ n까지의 parent를 자기자신으로 초기화
            size    : 1 ~ n까지 parent에 속한 개수를 1로 초기화 (자기자신 하나)

            sieve   : 에라토스테네스의 체. True로 남은 게 소수가 됨
        '''
        n = max(nums)
        given = set(nums)
        parent = list(range(n + 1))
        size = [1 for _ in range(n + 1)]

        sieve = [True for _ in range(n + 1)]
        sieve[0] = False
        sieve[1] = False
        # p: prime number.
        #    p의 배수 중 nums에 있는 걸 m1, ..., mk라 하면
        #    mk들은 모두 m1과 같은 parent를 가짐
        #    가장 작은 m은 2 * p이기 때문에 n // 2까지 탐색
        for p in range(2, n // 2 + 1):
            # for문 자체는 모든 수로 돌지만 소수만 쓰게 됨
            if sieve[p]:
                # p가 있으면 쓰고, 없으면 0으로 둠 (falsy)
                prev = p if p in given else 0
                # m: multiplier.
                for m in range(2 * p, n + 1, p):
                    sieve[m] = False
                    if m in given:
                        if prev:
                            union(prev, m)
                        else:
                            prev = m

        return max(size)
