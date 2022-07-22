import re

def solution(str1, str2):
    # 전처리한 문자열을 담아둘 s1, s2선언
    s1 = []
    s2 = []
    
    # 둘 중 더 긴 문장을 중심으로 2개씩 문자 나누기
    N = max(len(str1), len(str2)) - 1
    
    # 더 긴 문자열을 기준으로 루프를 돌며 전처리
    for i in range(N):
        
        # 어떤 문장이 더 긴 문장인지 알 수 없기 때문에
        # 문자열의 길이와 현재 인덱스를 비교하며 2개씩 나누기
        if len(str1) - 2 >= i:
            element1 = str1[i:i+2]
            
            # 현재 문자열에서 특수 문자들을 제거해준다
            # case 8번의 경우 _를 포함한 값을 전달하기 때문에 _를 추가로 제거해주었다
            remove_str1 = re.sub(r'[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·_]', '', element1)
            remove_str1 = re.sub(r'[0-9]', '', remove_str1)
            
            # 공백도 제거해준 후 길이가 2인 요소들만 s1에 추가한다
            if len(remove_str1.strip()) == 2:
                s1.append(element1)
        
        # str2도 똑같이 전처리해준다
        if len(str2) - 2 >= i:
            element2 = str2[i:i+2]
            remove_str2 = re.sub(r'[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·_]', '', element2)
            remove_str2 = re.sub(r'[0-9]', '', remove_str2)
            if len(remove_str2.strip()) == 2:
                s2.append(element2)
    # 교집합의 수를 나타내는 intersection,
    # 합집합의 수를 나타내는 union을 선언
    intersection = 0
    union = 0
    
    # s1과 s2를 돌며 소문자로 변환했을 때 동일한 문자열의 경우
    # s2에서만 제거해준다
    # 이 후 intersection에 1을 더해주어 교집합의 수를 구한다
    # 실행시간을 줄이기 위해 break를 통해 안쪽 for문을 나온다
    for i in s1:
        for j in s2:
            if i.lower() == j.lower():
                s2.remove(j)
                intersection += 1
                break
                
    # 위에서 중복되는 숫자는 모두 제거했기 때문에 
    # 합집합의 수는 s1과 s2를 더한 수가 된다
    union = len(s1) + len(s2)
    
    # 자카드 유사도를 구하여 답을 반환
    # 이 때 분모가 0이면 유사도가 1이므로 65536 반환
    return int(intersection / union * 65536) if union != 0 else 65536
