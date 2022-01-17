# 발표자 comment
# 행을 추가할때는 indexing을 써보는 것이 괜찮을것 같습니다.
# 아래 보다는
# for i in range(left, right):
#    curr_list.append(matrix[top][i])
# 아래와 같이 하는게 좀더 좋을것 같습니다.
# curr_list += matrix[top][left:right]
# tmi로 value만 추가할때에는 append가 빠르지만 list를 추가할때에는 +=이 빠릅니다.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 매트릭스의 top, left, bottom, right의 길이를 저장해줍니다.
        top, left, bottom, right = 0, 0, len(matrix), len(matrix[0])
        # 결과를 담을 리스트를 만들어줍니다.
        curr_list = []
        # top이 bottom보다 작을 때, left가 right보다 작을 때 루프문을 돌도록 설정해줍니다.
        while top < bottom and left < right:
            # 먼저 matrix의 첫번째 행을 모두 더해줍니다.
            for i in range(left, right):
                curr_list.append(matrix[top][i])
            # 이후 제일 위쪽의 행은 모두 추가했으므로 top에 1을 더해서 범위를 조정해줍니다.
            top += 1
            
            # top에서 bottom까지 루프를 돌며 각 행의 가장 오른쪽 숫자를 결과 리스트에 추가해줍니다.
            for i in range(top, bottom):
                curr_list.append(matrix[i][right-1])
            # 이후 right의 범위를 조정해줍니다.
            right -= 1
            
            # top과 left의 범위를 조정했으므로 right에서 left로, bottom에서 top으로 가는 방향을 돌기 전에 
            # 각 방향의 범위가 알맞게 조정이 됐는지 확인을 해줍니다.
            if not (top < bottom and left < right): break
            
            # 맨 밑 행에서 오른쪽에서 왼쪽으로 루프를 돌며 결과 리스트에 숫자를 추가해줍니다.
            for i in range(right-1, left-1, -1):
                curr_list.append(matrix[bottom-1][i])
            # bottom의 범위를 조정해줍니다.
            bottom -= 1
            
            # 마지막으로 bottom에서 top으로 가는 방향의 류프를 돌아줍니다.
            for i in range(bottom-1, top-1, -1):
                curr_list.append(matrix[i][left])
            # left의 범위를 조정해줍니다.
            left += 1
        
        return curr_list
