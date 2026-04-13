class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for i in range(len(l)):
            # l[i]부터 r[i]까지 슬라이싱 후, 정렬
            tmp = nums[l[i]:r[i]+1]
            tmp.sort()

            # 공차
            diff = tmp[1] - tmp[0]

            # 등차수열인지 확인
            tf = True
            for j in range(1, len(tmp)-1):
                if tmp[j+1] - tmp[j] != diff:
                    tf = False
                    break

            answer.append(tf)

        return answer
