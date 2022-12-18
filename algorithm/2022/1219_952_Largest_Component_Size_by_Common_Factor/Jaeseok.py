# test case 25개/125개만 성공..
# 문제를 제대로 이해하지 못함
# loop 자체의 거리를 찾아야 component가 되는데 그걸 고려하지 않음
from math import gcd


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0

        # 부모 노드를 찾으면서 동시에 부모 노드까지의 거리도 구함
        def find_parent(parent, x, l):
            if parent[x] != x:
                return find_parent(parent, parent[x], l+1)

            return x, l

        # 부모-자식관계를 형성하는 함수
        def union_parent(parent, a, b):
            a, _ = find_parent(parent, a, 0)
            b, _ = find_parent(parent, b, 0)
            if a < b:
                parent[b] = a
            else:
                parent[a] = b

        parent = [0] * (n)
        # 부모 테이블 초기화
        for i in range(n):
            parent[i] = i

        # 최대공약수가 1이 아니면 간선을 형성하도록 만듬
        vertex = []
        for i in range(n):
            for j in range(n-i):
                if gcd(nums[i], nums[i+j]) != 1:
                    vertex.append((i, i+j))

        # 만든 간선을 토대로 부모 테이블 갱신
        while vertex:
            a, b = vertex.pop()
            union_parent(parent, a, b)

        # 최대 길이가 answer
        for i in range(n):
            _, l = find_parent(parent, i, 1)
            if answer < l:
                answer = l
        return answer
