
class Solution:
    def pancakeSort(self, arr):
        
        # 비교 리스트
        ans = [i for i in range(1,len(arr)+1)]
        
        answer = []
        
        # 바꿀 필요 없으면 나감
        if arr == ans:
            return []
        
        # 역순으로 가면서 max값이 맨뒤로 가게 reverse
        for i in range(len(arr)-1,-1,-1):
            # 맨뒤가 max가 아니면 뒤집기
            if arr[i] != ans[i]:
                # 어디부터 뒤집을지 찾고
                reverse_num = arr.index(ans[i])+1
                
                # 뒤집어
                arr = list(reversed(arr[:reverse_num])) + arr[reverse_num:]
                answer.append(reverse_num)
                
                # 다시 뒤집으면 맨뒤로감
                arr = list(reversed(arr[:i+1])) + arr[i+1:]
                answer.append(i+1)
        return answer
