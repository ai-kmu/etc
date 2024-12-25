# 최종 풀이
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        if n == 1:
            return 0  # 한 명이면 바로 k연승

        champion = 0     # 0번 선수를 챔피언이라 가정
        streak = 0       # 현재 챔피언의 연속 승수

        # 1~n-1번 선수를 순회하며, 챔피언과 붙는 과정 시뮬레이션
        for i in range(1, n):
            if skills[champion] > skills[i]:
                # 챔피언이 계속 이김 -> streak + 1
                streak += 1
                # k연승 달성 시 즉시 종료
                if streak == k:
                    return champion
            else:
                # 새 challenger(i)가 이김 -> 챔피언 교체, streak=1
                champion = i
                streak = 1
                if streak == k:
                    return champion

        # 모든 선수를 한 번씩 상대해도 k연승이 안 나왔다면,
        # 더 이상 붙을 사람이 없으니 현재 champion이 최종 우승자
        return champion



# 실패 풀이
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        resulting_dict = dict()
        resulting_list = [idx for idx in range(len(skills))]
        win_count_list = [0] * len(skills)
        win_history_list = []
        is_duplication_detected = False
        duplication_list = []

        current_winner_idx = resulting_list.pop(0)

        while True:
            iter_cnt = 0
            if is_duplication_detected:
                observation_set = set()
                adding_list = [0] * len(skills)
                for elem in duplication_list:
                    observation_set.add(elem)
                    adding_list[elem] += 1

                max_idx = -1
                max_val = -1
                for idx, elem in enumerate(adding_list):
                    if elem > max_val:
                        max_val = elem
                        max_idx = idx

                return max_idx
            else:
                current_champions_continuous_win_cnt = 0
                for idx in range(len(skills) - 1):
                    current_candidate_idx = resulting_list.pop(0)

                    winners_skill = skills[current_winner_idx]
                    candidate_skill = skills[current_candidate_idx]
                    
                    if winners_skill > candidate_skill:
                        resulting_list.append(current_candidate_idx)
                        current_champions_continuous_win_cnt += 1
                    else:
                        resulting_list.append(current_winner_idx)
                        current_winner_idx = current_candidate_idx
                        current_champions_continuous_win_cnt = 0

                    win_count_list[current_winner_idx] += 1
                    win_history_list.append(current_winner_idx)

                    result_str = str(f"{current_winner_idx}{current_champions_continuous_win_cnt}{resulting_list[0]}")
                    current_champions_continuous_win_cnt = 0

                    if result_str in resulting_dict:
                        start_iter = resulting_dict[result_str]
                        # end_iter = iter_cnt
                        print("중복", result_str, resulting_dict, win_history_list[start_iter:])
                        duplication_list = win_history_list[start_iter:]
                        is_duplication_detected = True
                        break
                    else:
                        resulting_dict[result_str] = iter_cnt

                    if win_count_list[current_winner_idx] == k:
                        return current_winner_idx

                    iter_cnt += 1
