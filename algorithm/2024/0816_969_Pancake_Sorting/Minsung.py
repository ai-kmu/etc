class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        '''
        큰 수 부터 차례대로 정렬함
        Step 1
            - 정렬된 수를 제외한 가장 큰 수의 위치를 찾음
        Step 2
            - 정렬된 수를 제외한 가장 큰 수의 위치에서 pancake sort -> 정렬된 수를 제외한 가장 큰 수가 맨 앞으로 감
        Step 3
            - 정렬된 수를 제외한 가장 큰 수가 가야할 위치에서 pancake sort -> 맨 앞의 수와 가야 할 위치의 수가 바뀜
            - 정렬된 수에 해당 수를 추가함
        Step 1~3 반복
        '''
        ans = list()
        
        for i in list(range(1, len(arr)+1))[::-1]:  # 가장 큰 수부터 정렬시키기 위해 큰 수부터 시작
            # Step 1
            index = arr.index(i)  
            ans.append(index+1)  
            # Step 2
            arr = self.pancake_sort(arr, ans[-1])
            # Step 3
            ans.append(i)
            arr = self.pancake_sort(arr, ans[-1])

        return ans

    def pancake_sort(self, arr: List[int], target: int) -> List[int]:
        # 문제에 제시된 pancake sort 구현
        reversed_arr = arr[:target]
        reversed_arr = reversed_arr[::-1]
        reversed_arr[target:] = arr[target:]
        return reversed_arr
