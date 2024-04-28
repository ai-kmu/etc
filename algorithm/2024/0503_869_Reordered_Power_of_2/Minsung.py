class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        stage 1 : 
            주어진 n에서 0~9 빈도 수 저장
        stage 2 :
            문제 조건 하에 만들 수 있는 2의 제곱들 저장 -> self.pow
        stage 3 :
            각각의 2의 제곱의 0~9 빈도 수와 stage 1에서 구한 주어진 n의 0~9 빈도 수와 비교
        """
        ans = False  # 정답 value
        
        # stage 1
        nums = [0] * 10
        for i in str(n):
            nums[int(i)] += 1
        
        # stage 2
        self.pow = dict()
        self.make_pow_dict()
        self.pow = self.pow.keys()

        # stage 3
        for target in self.pow:
            target_nums = [0] * 10
            for i in target:
                target_nums[int(i)] += 1
            if nums == target_nums:
                ans = True
                break
        
        return ans

    def make_pow_dict(self):
        pow_index = 0
        while True:
            cur = str(2**pow_index)
            self.pow[cur] = True
            pow_index += 1
            if int(cur) >= 10**9:  # 문제 조건 제약 
                break
