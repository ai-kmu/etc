class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        # 오른쪽 부터 채우기
        # 오른쪽 부터 채울려면 왼쪽끝으로 보내야한다
        # 최대 2 번, 최소 1 번
        answer = []
        for j in range(len(arr)):
            target_num = len(arr) - j
            for i in range(target_num):
                # target num 찾으면
                if arr[i] == target_num:
                    # flip을 안해도 되면
                    if i + 1 == target_num:
                        break
                    # 맨 앞에 있으면
                    elif i != 0:
                        arr = arr[:i+1][::-1] + arr[i+1:]
                        answer.append(i+1)
                    arr = arr[:target_num][::-1] + arr[target_num:]
                    answer.append(target_num)
                    break    

        return answer
