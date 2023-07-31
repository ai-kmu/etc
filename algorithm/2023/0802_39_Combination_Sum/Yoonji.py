def combinationSum(candidates, target):
    # DFS 재귀 함수 정의
    def dfs(start, target, path):
        # target이 0이면 정답에 추가하고 반환한다.
        if target == 0:
            result.append(path)
            return

        # 현재 숫자부터 후보 배열 끝까지 반복하면서 탐색한다.
        for i in range(start, len(candidates)):
            # 후보 숫자가 target보다 크다면 넘어간다.
            if candidates[i] > target:
                continue
            # 현재 숫자를 path에 추가하고 target에서 현재 숫자를 빼면서 재귀 호출한다.
            dfs(i, target - candidates[i], path + [candidates[i]])

    # 최종 결과를 담을 리스트
    result = []
    # 후보 배열을 오름차순으로 정렬한다.
    candidates.sort()
    # DFS 알고리즘 호출
    dfs(0, target, [])
    # 결과 반환
    return result
