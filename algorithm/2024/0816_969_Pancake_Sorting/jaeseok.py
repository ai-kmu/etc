class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # 모든 숫자는 arr의 길이만큼 unique하게 존재함(1~len(arr))
        l = len(arr)
        traj = []
        while l != 0:
            # 현재 제일 큰 값의 인덱스를 찾음
            i = arr.index(l)
            # 그 인덱스까지 flip을 수행하고 traj에 추가 
            arr = arr[i::-1] + arr[i+1:]
            traj.append(i + 1)
            # 첫 인덱스로 이동한 가장 큰 값을 list 마지막으로 보내버리고 traj에 추가
            arr = arr[::-1]
            traj.append(l)
            # 마지막 인덱스로 간 현재 가장 큰 값은 더 건드릴 필요가 없으므로 그 앞부터 다시 반복
            arr = arr[:-1]
            # 이제 가장 큰 값은 현재 큰 값 - 1이므로 갱신
            l -= 1
        return traj
