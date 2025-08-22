class Solution(object):
    def calPoints(self, operations):
        result = []

        for idx, i in enumerate(operations):
            if i == "C":
                result = result[:len(result)-1]
            elif i == "D":
                tmp = 2 * int(result[len(result)-1])
                result.append(tmp)
            elif i == "+":
                tmp = int(result[len(result)-1]) + int(result[len(result)-2])
                result.append(tmp)
            else:
                result.append(int(i))

        return sum(result)
