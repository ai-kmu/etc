class Solution:
    def spiralOrder(self, matrix):
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        ans = []
        
        idx = 0
        while (len(ans) < len(matrix) * len(matrix[0])):
            if idx % 4 ==0:
                ans += matrix[top][left:right+1]
                top+=1
            elif idx % 4 ==1:
                ans += [d[right] for d in matrix[top:bottom+1]]
                right-=1
            elif idx % 4 ==2:
                ans += matrix[bottom][left:right+1][::-1]
                bottom-=1
            elif idx % 4 ==3:
                ans += [d[left] for d in matrix[top:bottom+1]][::-1]
                left += 1
            idx += 1
        return ans
