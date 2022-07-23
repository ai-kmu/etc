def create_set(string, length): # 단어 2개인 집합을 만드는 함수
    
    pair_set = []
    
    for i in range(length-1): # 두개씩 짜르면서 검사하는데,
        if string[i:i+2].isalpha(): # 만약 알파벳을 제외한 다른게 있으면 False임
            pair_set.append(string[i:i+2].upper()) # 대문자로 변환
    
    if len(pair_set) == 0: # 만약 E=M*C^2 이런게 들어오면 집합은 공집합이 됨.
        return ['@'] # 공집합을 나타내는 것.
    
    return pair_set

def solution(str1, str2):

    set_a = create_set(str1, len(str1)) # 집합으로 만들어주고
    set_b = create_set(str2, len(str2)) # 얘도 집합으로 만들어줌
    
    # print(set_a, set_b) 
    
    set_a.sort() # 정렬해야 조금 더 빠를 거임
    set_b.sort() # 왜냐면 밑에서 remove를 쓸건데, remove는 앞에서부터 찾아서 없애는 거라
                 # 정렬해놓고 remove하면 좀 더 빠르지 않을까? 싶어서 넣음 ㅇㅇ
    
    a = len(set_a)
    b = len(set_b)
    
    
    if a > b:
        long = set_a
        short = set_b
    else:
        long = set_b
        short = set_a
    
    # 긴거 짧은 거를 정하고
        
    long_len = len(long) # 가장 긴거의 길이를 구해놓음. 
        
    for i in short:
        try:
            long.remove(i)
        except:
            continue
    
    print(long)
    """
    쉽게 말하면, A n B = B - A 를 이용한거.
    len(B-A) 의 길이를 알아서 len(B)랑 빼주면
    교집합의 길이를 알 수 있음.
    
    그럼 합집합은 자동으로 
    
    len(A) + len(B-A) + len(A n B) 임.
    
    두 개를 얻었으니 계산하면 끝남 ㅇㅇ
    """
    intersect_len = long_len - len(long)
    
    union_len = len(short) + long_len - intersect_len
        
    return int((intersect_len/union_len) * 65536)
