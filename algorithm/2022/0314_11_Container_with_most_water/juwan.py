class Solution:
    def maxArea(self, height: List[int]) -> int:
        begin=0
        end=len(height)-1
        area=0
        while begin<end:
            print("area : ", area)
            print("min(height[beg],height[end])*(end-beg) : ",min(height[begin],height[end])*(end-begin))
            print("beg : ",begin)
            print("end : ", end)
            area=max(area,min(height[begin],height[end])*(end-begin))
            if height[begin]>height[end]:
                end=end-1
            else:
                begin=begin+1
        return area
