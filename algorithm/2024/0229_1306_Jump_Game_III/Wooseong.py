class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # DFS
        N = len(arr)
        
        queue = [start]
        visited = set()

        while queue:
            curr_ind = queue.pop()
            visited.add(curr_ind)

            # index 작아지는 방향
            left_ind = curr_ind - arr[curr_ind]
            # index 유효한 경우에만
            if 0 <= left_ind < N:
                # value 0이면 return True 종료
                if arr[left_ind] == 0:
                    return True
                # visited에 없으면 queue에 추가
                elif left_ind not in visited:
                    queue.append(left_ind)

            # 커지는 방향
            right_ind = curr_ind + arr[curr_ind]
            if 0 <= right_ind < N:
                if arr[right_ind] == 0:
                    return True
                elif right_ind not in visited:
                    queue.append(right_ind)
        
        return False

        # BFS
        N = len(arr)

        def bfs(start_ind):
            queue = [start_ind]
            visited = set()

            while queue:
                curr_ind = queue.pop()
                
                # 방문 체크
                if curr_ind in visited:
                    continue
                
                # index 유효한 경우에만
                if 0 <= curr_ind < N:
                    visited.add(curr_ind)

                    if arr[curr_ind] == 0:
                        return True

                    queue.append(curr_ind + arr[curr_ind])
                    queue.append(curr_ind - arr[curr_ind])

            return False

        return bfs(start)
