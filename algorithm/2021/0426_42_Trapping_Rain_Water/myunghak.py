class Solution:
    def trap(self, height):
        if len(height) <= 1:
            return 0
        ans = 0
        k = 0
        while(height[k] < height[k+1]):
            k+=1
            if k == len(height)-1:
                return 0
        
        start = [[height[k], 1]]
        
        for i in range(k+1, len(height)):
            # print("="* 20)
            # print(height[i], ans)
            # print(start)
            if height[i] > height[i-1]: # 만약 height가 증감하면
                M = min(height[i], start[0][0]) # 채울 물의 높이는 height 혹은 start[0]중 작은 쪽을 따른다.
                S = 0
                for j in range(1, len(start) + 1): #  M과 높이와 같은 높이까지 다 물을 채움
                    if start[-j][0] > M:
                        start[-j+1:] = [[M,S+1]]
                        break
                    else:
                        S += start[-j][1]
                        ans += (M-start[-j][0])*start[-j][1]
                        if j == len(start): # 만약 다 비웠다면
                            # print("all clear")
                            
                            start = [[height[i], 1]]
                
            else: # 만약 height가 감소하면
                start.append([height[i], 1])
            
        return ans
