from collections import deque
class Solution(object):
    # @staticmethod
    # def distance_func(num1, num2):
    #     distance = 0
    #     num1_plus_10 = [10+i for i in num1]
    #     for position, num in enumerate(num2):
    #         distance += min(abs(num1[position] - num) , abs(num1_plus_10[position] - num))
    #     return distance

    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        # 가장 짧은거리 탐색 -> bfs

        memo = deque([[0,'0000']]) # step, num
        deadends_set = set(deadends)
        step = 0 
        while 1:    

            # 종료조건, 길이 막힘
            if len(memo) == 0:
                return -1

            step, cur_num = memo.popleft()

            # 답을 찾음
            if cur_num == target:
                return step

            # 방문 처리
            if cur_num in deadends_set:
                continue
            deadends_set.add(cur_num)


            if step == 30:
                return None

            # 4개에 대해서 탐색
            for position in range(4):
                # move
                for di in [1, -1]:
                    cur_list = list(cur_num)
                    cur_list[position] = str((int(cur_list[position]) + di)%10)
                    next_num = ''.join(cur_list)
                    # 못가면
                    if next_num in deadends_set:
                        continue
                    # 갈 수 있으면
                    else:
                        memo.append([step+1, next_num])
                        
        return -1
        
