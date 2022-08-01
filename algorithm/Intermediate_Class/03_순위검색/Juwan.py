from collections import defaultdict

def solution(info, query):
    
    mapping = {'-':'1','cpp' : '2', 'java': '3', 'python':'4',
           'backend':'2', 'frontend':'3', 'junior':'2','senior':'3',
           'chicken':'2', 'pizza':'4'}
    info_dict = {}
    
    
    
    for i in range(len(info)):
        
        splits = info[i].split()
        info_dict[mapping[splits[0]] + mapping[splits[1]] + mapping[splits[2]] + mapping[splits[3]]] = int(splits[4])
        
    print(info_dict)
    
    # 효율성 극복 못함
    # -> 다른 풀이를 하려했으나 실패
