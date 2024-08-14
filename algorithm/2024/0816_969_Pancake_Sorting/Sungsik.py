class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # 최대 2n이 나오는 풀이
        max_num = len(arr)
        answer = []
        target = list(range(1, max_num+1))
        
        # 최댓값을 list의 맨 뒤로 보내고
        # 최댓값을 1씩 줄여나가는 방식
        while arr != target:
            idx = arr.index(max_num) + 1
            if idx != max_num:
                arr = list(reversed(arr[:idx])) + arr[idx:]
                answer.append(idx)
                arr = list(reversed(arr[:max_num])) + arr[max_num:]
                answer.append(max_num)
            max_num -= 1
        return answer
        
        
