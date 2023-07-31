# testing만 통과, 코드리뷰 안해주셔도 됩니다
class Solution(object):
    def combinationSum(self, candidates, target):
        def recurrent(start, target, path):

            # target이 0이면 현재 path는 결과에 추가 가능한 조합
            if target == 0:
                result.append(path[:])
                return

            # candidates 배열 반복
            for i in range(start, len(candidates)):
                # 현재 숫자가 남은 target보다 크면 종료
                if candidates[i] > target:
                    break

                # 현재 숫자를 path에 추가
                path.append(candidates[i])

                # 재귀적 호출
                # target에서 현재 숫자를 빼주어 새로운 target으로 설정
                recurrent(i, target - candidates[i], path)

                # 이후 현재 숫자를 path에서 제거
                path.pop()

        result = []
        recurrent(0, target, [])

        return result
