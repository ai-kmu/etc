class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # 결과를 저장할 빈 리스트를 초기화
        ans = []
        
        # 주어진 이진 문자열 배열 nums의 길이만큼 반복
        for i in range(len(nums)):
            # i번째 이진 문자열에서 i번째 위치의 문자를 가져옴
            curr = nums[i][i]
            
            # 현재 문자가 "0"이면 "1"을, "1"이면 "0"을 ans 리스트에 추가 (비교된 위치에 대한 반대값을 추가)
            ans.append("1" if curr == "0" else "0")
        
        # 리스트에 저장된 값을 문자열로 변환하여 반환
        return "".join(ans)
