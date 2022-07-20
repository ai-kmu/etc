def solution(clothes):
    clothes_type = dict()
    for i in range(len(clothes)):
        if clothes[i][1] in clothes_type:
            clothes_type[clothes[i][1]] += 1
        else: 
            clothes_type[clothes[i][1]] = 2
    aws = 1
    for i in list(clothes_type.values()):
        aws *= i
    return aws - 1
