class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        # nums 안의 2진수 str을 실제 10진수로 채워넣도록 bin_nums를 선언
        bin_nums = []
        for i in nums:
            bin_nums.append(int(i, 2))
        # 0부터 1씩 더해가면서 bin_nums에 없는 10진수를 찾음
        answer = 0
        while answer < 2 ** 16:
            # nums의 길이와 정답 2진수의 자릿수가 같으므로 zfill로 나머지 부분을 채워줌
            if answer not in bin_nums:
                return(bin(answer)[2:].zfill(n))
            answer += 1
          
