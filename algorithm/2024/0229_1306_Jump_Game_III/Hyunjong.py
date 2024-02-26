class Solution(object):

    def dfs(self, start_index, arr, visited):
        # 시작점이 0이면 
        if arr[start_index] == 0:
            return True

        # start_index에 빼고 더할 값
        value = arr[start_index]

        # 갈 수 있는 2가지 위치
        front_index = start_index - value
        back_index = start_index + value
        
        # 앞 번호가 범위내에 있고 방문안했으면
        if front_index >= 0 and front_index < len(arr) and front_index not in visited:
            # 방문 처리
            visited.add(front_index)
            # 만약 dfs 결과가 true이면 return true
            if self.dfs(front_index, arr, visited):
                return True
        
        # 뒷 번호가 범위내에 있고 방문 안했으면
        if back_index >= 0 and back_index < len(arr) and back_index not in visited:
            # 방문 처리
            visited.add(back_index)
            # 만약 dfs 결과가 true이면 return true
            if self.dfs(back_index, arr, visited):
                return True
                
        # 다 돌았을 때 없으면 False
        return False

    def canReach(self, arr, start):
        visited = set()
        return self.dfs(start, arr, visited)
