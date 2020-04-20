from copy import deepcopy
import re

actual_banned_ids = []


def determine_n_combination(overall_candidates):
    actual_banned_ids = []
    def check(idx, candidates, cur_set):
        if idx == len(candidates):
            if cur_set not in actual_banned_ids:
                actual_banned_ids.append(deepcopy(cur_set))
            return
        for actual_id in candidates[idx]:
            if actual_id not in cur_set:
                cur_set.add(actual_id)
                check(idx + 1, candidates, cur_set)
                cur_set.remove(actual_id)
    
    check(0, overall_candidates, set())
    return len(actual_banned_ids)

def solution(user_ids, banned_ids):
    generate_regular_expression = lambda _id: re.compile("^" + _id.replace("*", "([0-9]|[a-z])") + "$")
    regex_banned_ids = list(map(generate_regular_expression, banned_ids))
    overall_candidates = []
    for regex_banned_id in regex_banned_ids:
        candidates = []
        for user_id in user_ids:
            if regex_banned_id.match(user_id):
                candidates.append(user_id)
        overall_candidates.append(candidates)
    
    return determine_n_combination(overall_candidates)
