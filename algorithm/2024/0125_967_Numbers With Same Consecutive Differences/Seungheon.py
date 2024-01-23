class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        answer = []
        tmp_set = set()

        def explore(str_num):
            # 중복제거
            if str_num in tmp_set:
                return
            else:
                tmp_set.add(str_num)
            
            # 탈출조건
            if len(str_num) == n :
                answer.append(int(str_num))
                return
            
            # 탐색
            up_num = int(str_num[-1]) + k
            down_num = int(str_num[-1]) - k
            if up_num < 10:
                explore(str_num + str(up_num))
            if down_num >= 0:
                explore(str_num + str(down_num))

        for i in range(1,10):
            explore(str_num=str(i))

        return answer
                
