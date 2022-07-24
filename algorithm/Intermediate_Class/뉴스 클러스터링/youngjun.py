from itertools import repeat
import re

def solution(str1, str2):
    str1_list = []
    str2_list = []
    intersect_many = []
    union_many = []
    
    str1 = str1.upper()
    str2 = str2.upper()

    for i in range(len(str1)-1):
        if re.search('[^a-zA-Z]', str1[i:i+2]) == None:
            str1_list.append(str1[i:i+2])
    
    for i in range(len(str2)-1):
        if re.search('[^a-zA-Z]', str2[i:i+2]) == None:
            str2_list.append(str2[i:i+2])
    
    if len(str1_list) == 0 and len(str2_list) == 0:
      
        return 65536
    
    else:
        intersect = list(set(str1_list)&set(str2_list))
        union = list(set(str1_list)|set(str2_list))

        for i in intersect:
            intersect_many += list(repeat(i,min(str1_list.count(i),str2_list.count(i))))
    
        for i in union:
            union_many += list(repeat(i,max(str1_list.count(i),str2_list.count(i))))
            
        answer = int(len(intersect_many)/len(union_many) * 65536)
        
        return answer
