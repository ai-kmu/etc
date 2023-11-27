class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        a = []

        for i, g in enumerate(gas):
            for j, c in enumerate(cost):
                if i == j:
                    a.append(g-c)
                else:
                    continue
        tot = 0
        posit = []
        for i, _ in enumerate(a):
            if _ > 0:
                posit.append(i)
        print(a)
        for i, _ in enumerate(posit):
            arr = a[_:]+a[:_]
            tot = 0
            print(arr)
            for j in arr:
                tot += j
                print(tot)
                if tot <= 0:
                    break
            return _
        return -1
