class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        k_list = []
        length = len(arr)

        if arr == list(sorted(arr)):
            return k_list
        
        # 큰 수부터 뒤로 밀기
        # 1. 큰 수부터 위치를 찾아 해당 index를 뒤집기 -> 그 수가 맨 앞으로 옴
        # 2. 그 수만큼 다시 뒤집기 -> i번째 값이 i번째 위치로 이동
        # 3. 반복
        for i in range(length, 1, -1): 
            pos = arr.index(i)
            # 1
            arr[:pos + 1] = arr[:pos + 1][::-1]
            k_list.append(pos + 1)
            # 2
            arr[:i] = arr[:i][::-1]
            k_list.append(i)

        return k_list
