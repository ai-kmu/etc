class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        answer = ""
        nums = [i for i in range(1, n + 1)]
        
        for i in range(1, n + 1):
            idx = 0
            # 앞을 고정했을 때 뒤에 올 수 있는 가능한 순열의 개수 모두 구하기
            c = math.factorial(n - i)

            # 찾고자 하는 인덱스보다 뒤에 올 수 있는 개수가 크면 고정 값을 추가하기
            while c < k:
                idx +=1
                k -= c
                
            # 고정 값을 정닶이 반영
            answer += str(nums[idx])
            del nums[idx]
            
        return answer
