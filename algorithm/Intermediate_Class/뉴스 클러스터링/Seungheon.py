from collections import defaultdict 
def solution(str1, str2):
    
    # key set
    key_set = set()

    # 순회하며 key를 알아낸다.
    # dictionary에 값들 추가
    def make_dict(string):
        nonlocal key_set
        str_dict = defaultdict(int)
        for i in range(len(string)-1):
            c_point = False
            key = string[i:i+2].upper()
            if list(filter(lambda x :ord(x)<65 or ord(x)>90, key)):
                continue
            str_dict[key] += 1
            key_set.add(key)
        return str_dict
    
    # dictionary 만들기
    dict1 = make_dict(str1)
    dict2 = make_dict(str2)

    # 교집합
		# 합집합
    intersection_set = 0
    sum_set = 0
    key_list = list(key_set)
    
    for k in key_list:
        # 두 string에 모두 있으면 작은값을 교집합에 추가
        if dict1[k] and dict1[k]:
            intersection_set += min(dict1[k], dict2[k])
        # 다른값들은 합집합에 추가
        sum_set += max(dict1[k], dict2[k])
        
    return int((intersection_set/sum_set)*65536) if sum_set else 65536
