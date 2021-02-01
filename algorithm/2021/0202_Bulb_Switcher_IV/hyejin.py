class Solution:
    def minFlips(self, target: str) -> int:
        # 이 문제는 serial하게 풀 수 있는 문제
        
        filp = False # False는 0, True 1
        count = 0
        # for문 돌면서 뒤집어줘야 되는경우 뒤집고 아니면 넘어감
        for i in target:
            if i == "1" and filp is False:
                count += 1
                filp = True
            elif i == "0" and filp is True:
                count += 1
                filp = False
                
        return count
