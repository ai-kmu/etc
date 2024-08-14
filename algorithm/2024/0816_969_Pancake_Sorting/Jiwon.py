class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        answer = []

        if arr == sorted(arr):
            return answer

        # 배열의 가장 큰 값부터 정렬 시작      
        for max_value in range(max(arr), 1, -1):
            max_idx = arr.index(max_value)
            
            # max value가 제 자리에 잘 있는 경우
            if max_idx + 1 == max_value:
                continue
            else:
                # 정렬 안 된 max_value 값이 0번에 없으면 0번으로 옮기고 뒤집기
                if max_idx != 0:
                    k = max_idx + 1
                    answer.append(k)
                    arr = arr[:k][::-1] + arr[k:]

                k = max_value
                answer.append(k)
                arr = arr[:k][::-1] + arr[k:]

        return answer
        
