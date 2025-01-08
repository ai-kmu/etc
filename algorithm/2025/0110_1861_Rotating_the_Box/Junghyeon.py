'''
루프 순회하면서 "#"과 "."을 각각 따로 저장
"*"를 만났을때, "#" 리스트와 "." 리스트가 둘 다 있으면 *를 기준으로 왼쪽에서부터 "#" 리스트에서 "#"을 꺼내 모두 채우고, "." 리스트에서 "."를 꺼내 모두 채움 (idx-1)
마찬가지로 행의 끝에 오면 현재 인덱스에서 "#" 리스트에서 "#"을 꺼내 모두 채우고, "." 리스트에서 "."를 꺼내 모두 채움 (idx)
'''

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # 
        for row_num, row in enumerate(boxGrid):
            stack_dot = []
            stack_bar = []
            for idx in range(len(row)):
                curr = row[idx]
                if curr == "#":
                    stack_dot.append(curr)
                if curr == ".":
                    stack_bar.append(curr)
                if curr == "*" or idx == len(row)-1:
                    if stack_dot and stack_bar:
                        # print(row_num, idx, stack_dot, stack_bar)
                        if curr == "*":
                            start_point = idx-1
                            for dot in stack_dot:
                                boxGrid[row_num][start_point] = dot
                                start_point -= 1
                            for bar in stack_bar:
                                boxGrid[row_num][start_point] = bar
                                start_point -= 1
                        else:
                            start_point = idx
                            for dot in stack_dot:
                                boxGrid[row_num][start_point] = dot
                                start_point -= 1
                            for bar in stack_bar:
                                boxGrid[row_num][start_point] = bar
                                start_point -= 1
                    stack_dot = []
                    stack_bar = []

        result = []
        
      # 90도 회전하는 리스트 만드는 루프
        for i in range(len(boxGrid[0])):
            gggrrrrow_numiddd = []
            for j in range(len(boxGrid)-1, -1, -1):
                gggrrrrow_numiddd.append(boxGrid[j][i])
            result.append(gggrrrrow_numiddd)

        return result
