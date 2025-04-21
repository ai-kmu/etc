from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for i in s:
            d1[i] += 1
        
        for i in t:
            d2[i] += 1
        
        # print(d1)

         #print(d2)

        d1_list = []
        d2_list = []

        for k, v in d1.items():
            d1_list.append([k, v])

        for k, v in d2.items():
            d2_list.append([k, v])

        d1_list.sort()
        d2_list.sort()

        # print(d1_list)
        # print(d2_list)

        if len(d1_list) == len(d2_list):
            for i, j in zip(d1_list, d2_list):
                if i[1] != j[1]:
                    return i[0]
        else:
            for i, j in zip(d1_list, d2_list):
                if i[0] != j[0]:
                    return i[0]

        return d2_list[-1][0]
