# 야매방법
class Solution(object):
    def findSecondMinimumValue(self, root):
        # print(str(root))
        root = str(root).split(' ')

        num = set()

        for i in root:
            try:
                num.add(int(i[:-1]))
            except:
                continue

        num = sorted(list(num))
        if len(num) < 2:
            return -1
        return num[1]    
