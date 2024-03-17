class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 핵심 아이디어
        # k개의 홀수의 개수를 만족하는 부분 배열을 찾아 그 앞쪽의 (짝수 개수+1)와 그 뒤쪽의 (짝수 개수+1)를 곱해준다. 
        # 단, continuous한 성질을 만족해야 한다. 
        # 이를 반복
        check = []  # 홀수인지 짝수인지 체크하는 배열
        for i in nums:
            if i%2 == 1:
                check.append(1)
            else:
                check.append(0)

        tmp = []  # 홀수의 갯수와 홀수의 idx를 튜플의 형태로 저장하는 list
        cnt = 0  # 홀수 갯수 cnt
        ans = 0  # 정답 값 저장
        start_idx = 0  # 홀수 값이 시작하는 idx
        even_left = 0  # 부분 배열 앞 쪽의 짝수 개수 
        even_right = 0  # 부분 배열 뒤 쪽의 짝수 개수 

        for i in range(len(nums)):
            if check[i] == 1:
                cnt = cnt + 1
                tmp.append((cnt, i))
            if cnt == k:
                for j in range(tmp[0][1]-1, -1, -1):
                    if check[j] == 0:
                        even_left = even_left + 1
                    else:  # continuous한 성질을 만족해야 하므로
                        break
                for j in range(i+1, len(nums), 1):
                    if check[j] == 0:
                        even_right = even_right + 1
                    else:  # continuous한 성질을 만족해야 하므로
                        break
                ans = ans + (even_left+1)*(even_right+1)
                cnt = cnt-1
                del tmp[0]
                even_left = 0
                even_right = 0
        return ans
                

                    
