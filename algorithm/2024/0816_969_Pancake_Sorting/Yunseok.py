class Solution:
    def __init__(self):
        self.returning_arr = []

    def reverse(self, arr, k): # k번째 요소까지 뒤집기
        return arr[:k][::-1] + arr[k:]

    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)

        # 가장 큰 값을 앞으로 보낸 후, 이를 제일 뒤로 보내는 작업 수행
        for current_window in range(n, 1, -1):
            biggest_val = max(arr[:current_window])
            biggest_val_idx = arr.index(biggest_val)
            
            if biggest_val_idx != current_window - 1:
                # 가장 큰 값이 배열의 첫 번째 위치에 있지 않으면, 이를 첫 번째로 이동
                if biggest_val_idx != 0:
                    k = biggest_val_idx + 1
                    arr = self.reverse(arr, k)
                    self.returning_arr.append(k)
                
                # 가장 큰 값을 배열의 마지막 위치로 이동
                arr = self.reverse(arr, current_window)
                self.returning_arr.append(current_window)

        return self.returning_arr
