class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """

        # 오른쪽 부터 채우기
        # two pointer
        # 채울 위치 : swap_point
        #   - 처음 swap_point는 오른쪽 끝
        #   - 돌을 만나면 돌 위치를 변경 & swap_point를 한칸 더 이동 # swap_point 이동시에는 끝까지 왔는지. 돌이 없는지 확인하고 적절하게 처리 
        # 돌 위치 : cur_point

        # 돌이 있으면 돌이
        def check_obj(point, row_i, obj= '.'):
            col = point
            if not boxGrid[row_i][col] == obj: # 빈공간이 아니면
                return False
            else:
                return True

    
        for row_i, row in enumerate(boxGrid):
            right_point = -1 # 오른쪽 끝부터
            left_point = -2
            try:
                while 1:
                    # left_point # 돌 만날때 까지 진행 # left point
                    while 1: # left_point가 왼쪽 끝으로 오면 종료
                        # 종료 조건
                        # left point
                        if check_obj(left_point, row_i, '#'): # 돌    
                            break
                        elif check_obj(left_point, row_i, '*'): # 벽
                            right_point = left_point - 1
                            left_point = right_point - 1
                        elif check_obj(left_point, row_i, '.'): # 빈 공간
                            left_point -= 1

                    # right_point # 빈공간 만날때 까지 진행 # right point
                    while left_point < right_point: # right_point == left point 가 되면 종료

                        # 종료 조건
                        # right_point
                        if check_obj(right_point, row_i, '.'): # 빈 공간이면
                            break
                        else:
                            right_point -= 1

                    boxGrid[row_i][left_point] = '.'
                    boxGrid[row_i][right_point] = '#'
                    left_point -= 1
                    right_point -= 1
            except:     
                continue

        return [list(row) for row in zip(*boxGrid[::-1])]
            
