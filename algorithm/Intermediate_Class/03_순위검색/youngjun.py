# 1. hash table을 만들어 줌으로서 query 검색을 빠르게 하도록 한다.
# 2. query에서 score를 검색할 시, 이분 탐색을 활용하여 탐색 시간을 줄이도록 한다.
from itertools import combinations
from collections import defaultdict

def make_info_to_hash_table(information, dictionary):
    # info 하나하나 순회하면서
    for i in information:
        # 띄어쓰기를 기준으로 split 해준다.
        info_temp = i.split(" ")
        # info의 점수조건을 score로, 나머지 조건들을 condition으로 설정한다.
        condition, score = info_temp[:-1], int(info_temp[-1])
        # query의 질문과 같은 꼴을 만들어 주기 위해, combination을 활용하여 condition key를 만들어준다.
        for n in range(5):
            # 우선 0 부터 3까지 1개, 2개, 3개, 4개를 뽑을 수 있는 경우의 수를 combination를 활용해 구해준다.
            # 이를 combi 라고 한다.
            combi = list(combinations(range(4),n))
            # 각각의 경우의 수(combi)를 순회하면서
            for c in combi:
                # condition_key인 'case'를 초기화한 다음
                case = ''
                # 0부터 3까지 순회하면서
                for j in range(4):
                    # j가 combi 안에 있을 경우
                    if j in c:
                        # case에 condition의 j번째 원소를 더한다.
                        case += condition[j]
                    # j가 combi 안에 있지 않을 경우
                    else:
                        # case에 -를 더한다.
                        case += '-'
                # condition key인 'case'가 다 만들어졌으면, 각각 주어진 score list 안에 score를 넣는다.
                dictionary[case].append(score)
    # 만들어진 hash table 반환한다.
    return dictionary

def info_sort(dictionary):
    # hash_table의 key를 순회하면서
    for key in dictionary.keys():
        # 각 key 마다의 score list를 정렬해준다.
        dictionary[key] = sorted(dictionary[key])
    # score list가 정렬된 hash table을 반환한다.
    return dictionary

# lower bound 이진탐색
def low_bound_binary_search(target,list):
  # 이진 탐색에 앞서 low index와 high index 설정
  # low는 0으로 초기화한다.
  # high는 target이 list에 없는 큰 값일 수 있기 때문에, 가장 큰 index + 1을 해준다.
  low, high = 0, len(list)
  # low가 high 보다 작은 동안 계속 탐색한다.
  while low < high:
      # mid index 설정
      mid = (low + high) // 2
      # 만약 target이 list의 mid index 번째 값보다 클 경우
      if target > list[mid]:
          # low를 mid + 1로 설정한다.
          low = mid + 1
      # 만약 target이 list의 mid index 번째 값보다 작거나 같을 경우
      if target <= list[mid]:
          # high를 mid로 설정한다.
          high = mid
  # 탐색이 끝나면 low bound인 high를 반환한다.
  return high

def query_search(query, dictionary, output):
    # 쿼리 하나하나 순회하면서
    for q in query:
        # 띄어쓰기를 기준으로 split 해준다.
        query_temp = q.split(" ")
        # 쿼리의 점수조건을 q_score로, 나머지 조건들을 q_order로 설정한다.
        q_order, q_score = query_temp[:-1], int(query_temp[-1])
        # q_order에서 and를 삭제한다.
        for _ in range(3):
            q_order.remove('and')
        # list인 q_order를 string 형태로 만들어준다.
        q_case = ''.join(q_order)
        # q_case가 위에서 만든 hash table의 키일 경우
        if q_case in dictionary.keys():
            # 탐색할 리스트는 info hash table을 q_case로 검색했을 때의 score list이다.
            score_list = dictionary[q_case]
            # 여기서 target은 쿼리의 점수조건이다.
            score_target = q_score
            # 위에서 구한 score list의 길이를 계산한다.
            score_length = len(score_list)
            # 이진 탐색을 통해 low bound 탐색을 하여, low bound index를 구한다.
            target_low_index = low_bound_binary_search(score_target, score_list)
            # 위에서 구한 score list의 길이에서 low bound index를 빼주어 q_num을 계산한다.
            q_num = score_length - target_low_index
            # 계산된 q_num을 output에 append 해준다.
            output.append(q_num)
        # q_case가 위에서 만든 hash table의 키가 아닐 경우
        else:
            # 0을 output에 append 해준다.
            output.append(0)
    # output 반환
    return output

def solution(info, query):
    # hash table 초기화
    # 점수가 갱신되지 않고 하나하나 모두 저장될 수 있도록, value 값을 list 형태인 score list로 만들어준다.
    info_dict = defaultdict(list)
    # 정답 list 초기화
    answer = []
    
    # info를 query와 비슷한 꼴로 만들어 hash table인 info_dict를 만들어준다.
    make_info_to_hash_table(info, info_dict)
    
    # info_dict의 value 값인 score list를 정렬해준다.
    info_sort(info_dict)
    
    # info_dict의 query문을 검색한 후, 점수 조건을 맞춘 answer list를 반환한다.
    query_search(query, info_dict, answer)
    
    # 정답 list를 반환한다.
    return answer
