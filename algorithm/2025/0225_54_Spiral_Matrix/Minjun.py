class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        tot = len(matrix) * len(matrix[0])
        circle = 0
        st = 0
        end = len(matrix[0])-1
        direction = 'down'
        idx = 0
        fivot = len(matrix) -1
        while matrix:
            if len(ans) == tot:
                return ans
            if direction == 'down':
                if idx == 0: # right
                    ans.extend(matrix[idx][st:end+1])
                    idx += 1
                elif idx == fivot: # left
                    if st == 0:
                        ans.extend(matrix[idx][::-1])
                    else:
                        ans.extend(matrix[idx][end:st-1:-1])
                    direction = 'up'
                else: # 내려가는 중
                    ans.append(matrix[idx][end])
                    idx += 1
            elif direction == 'up':
                if idx-1 == 0: # 처음 도달
                    circle+=1
                    idx-= 1
                    direction = 'down'
                    del matrix[0]
                    del matrix[-1]
                    fivot -= 2
                    st += 1
                    end -= 1
                else: # 올라가는 중
                    idx -= 1
                    ans.append(matrix[idx][st])

        return ans
