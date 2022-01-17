class Solution:
    def spiralOrder(self, matrix):
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        ans = [0 for _ in range(len(matrix) * len(matrix[0]))]
        
        idx = 0
        size = 0
        while (size < len(matrix) * len(matrix[0])):
            print(ans)
            if idx % 4 ==0:
                ans[size:size-left+right+1] = matrix[top][left:right+1]
                size += right+1 - left
                top+=1
            elif idx % 4 ==1:
                ans[size:size+bottom-top+1] = [d[right] for d in matrix[top:bottom+1]]
                size += bottom+1 - top
                right-=1
            elif idx % 4 ==2:
                ans[size:size-left+right+1] = matrix[bottom][left:right+1][::-1]
                size += right+1 - left
                bottom-=1
            elif idx % 4 ==3:
                ans[size:size+bottom-top+1] = [d[left] for d in matrix[top:bottom+1]][::-1]
                size += bottom+1 - top
                left += 1
            idx += 1
        return ans
