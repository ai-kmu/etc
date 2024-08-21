# timelimit(552 / 564 testcases passed)

class Solution(object):
    def miceAndCheese(self, reward1, reward2, k):
        """
        :type reward1: List[int]
        :type reward2: List[int]
        :type k: int
        :rtype: int
        """
        answer = []
        temp = []
        remove_num = []
        n = len(reward1)
        

        for i in range(n):
            temp.append(reward1[i]-reward2[i])
        
        for j in range(k):
            num = temp.index(max(temp))
            del(temp[num])
            answer.append(reward1[num])
            del(reward1[num])
            del(reward2[num])


        
        return sum(answer+reward2)
