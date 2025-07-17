class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ret = [] # 결과 반환 list

        def combiSum(k, n, s, l):
            nonlocal ret
            
            if n < 0:
                return
            
            elif k == 0 and n == 0: # k와 n 모두 만족 시에만 리스트에 추가
                ret.append(l)

            else:
                for new_s in range(s, 10):
                    combiSum(k - 1, n - new_s, new_s + 1, l + [new_s])
                return


        for i in range(1, 10): # 시작 값 i 미리 추가하여 함수 실행
            combiSum(k - 1, n - i, i + 1, [i])

        return ret
