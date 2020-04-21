from copy import deepcopy
import re

def determine_n_combination(overall_candidates):
    # T(this part) = In worst case, O(len(user_ids)^len(user_ids))
    actual_banned_ids = set()
    def check(idx, cur_set):
        # Variant DFS
        if idx == len(overall_candidates):
            if str(cur_set) not in actual_banned_ids:
                actual_banned_ids.add(str(deepcopy(cur_set)))
            return
        for actual_id in overall_candidates[idx]:
            if actual_id not in cur_set:
                cur_set.add(actual_id)
                check(idx + 1, cur_set)
                # backtracking
                cur_set.remove(actual_id)
    
    check(0, set())
    return len(actual_banned_ids)

def solution(user_ids, banned_ids):
    # T(this part) = O(len(banned_ids) * 2^m) <= O(len(user_ids) * 2^m)
    # 일반적으로(언어의 구현체를 무시하고, 효율적인 구현 방법으로는)
    # regular expression의 compile에는 O(2^m)의 시간이 소요된다. (m은 regular expression의 길이)
    # 또한 len(banned_ids) 개의 regular expression 을 compile해야하므로 전체적으로 O(len(banned_ids) * 2^m)이 소요된다고 할 수 있다.
    generate_regular_expression = lambda _id: re.compile("^" + _id.replace("*", "([0-9]|[a-z])") + "$")
    regex_banned_ids = list(map(generate_regular_expression, banned_ids))
    
    # T(this part) = O(len(user_ids)^2)
    overall_candidates = []
    for regex_banned_id in regex_banned_ids:
        candidates = []
        for user_id in user_ids:
            # 일반적으로(언어의 구현체를 무시하고, 효율적인 구현 방법으로는)
            # regex 를 match할 때는 O(n)의 시간이 소요된다. (n은 match 대상 문자열의 길이)
            if regex_banned_id.match(user_id):
                candidates.append(user_id)
        overall_candidates.append(candidates)
    
    
    return determine_n_combination(overall_candidates)
