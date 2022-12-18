from collections import deque, defaultdict


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        # union-find로 해결해보려고 했지만 time error
        if 1 in nums:
            nums.remove(1)
        
        n = len(nums)
        max_num = max(nums)
        max_divisor = max_num // 2

        # 둘 사이의 edge 여부를 판단해야 하는데
        # 모두 다 나눠보면 비효율적이므로
        # 에라토스테네스의 체를 이용하여 소수를 구함
        is_prime = [True] * (max_divisor + 1)
        divisor_dict = defaultdict(list)
        for i in range(2, max_divisor+1):
            if is_prime[i]:
                # 각 소수마다 나눠떨어지는 숫자들을 dictionary에 list 형태로 추가
                for num in range(n):
                    if nums[num] % i == 0:
                        divisor_dict[i].append(num)
                if i * i <= max_num:
                    for j in range(2 * i, max_divisor, i):
                        is_prime[j] = False
        
        parents = list(range(n))
        size = [1] * n

        def find(node):
            while parents[node] != node:
                node = parents[node]
            return node
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 != parent2:
                if size[node1] > size[node2]:
                    parents[parent2] = parent1
                    size[parent1] += size[parent2]
                else:
                    parents[parent1] = parent2
                    size[parent2] += size[parent1]

        edges = set()
        # 각 소수인 약수마다 나눠떨어지는 숫자 리스트를 확인
        for divisor, node_list in divisor_dict.items():
            # 첫번째 숫자를 기준으로
            node = node_list[0]
            # 나머지 숫자들을 합침
            for other in node_list[1:]:
                if (node, other) not in edges:
                    union(node, other)
                    edges.add((node, other))

        return max(size)


        
