import itertools
import copy


class Solution:
    '''
    스트링을 문자단위로 쪼개고 사이에 공백을 넣어 리스트를 만든다.
    ex -> ['0', '', '0', '', '0', '', 0, '']
    공백에 '.'를 추가하여 가능한 ip주소들을 만들고, 그것이 유효한 ip인지 확인
    '''
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(ip):
            tmp = ip.split('.')
            for num in tmp:
                # 1. '123.0.0.'처럼 스트링의 맨 뒤에 '.'이 오는 경우
                # 2. '123.01.01.01' 처럼 수의 맨 앞자리에 0이 오는 경우
                # 3. '300.300.300.0' 처럼 수의 크기가 255를 넘어가는 경우
                if num == '' or str(int(num)) != num or int(num) > 255:
                    return False
            return True
        
        new_s = list()
        result = list()
        arr = [i for i in range(len(s))]
        # 가능한 모든 조합의 수를 리스트로 만들어 저장 C(len(s), 3)
        comb_list = list(itertools.combinations(arr, 3))
        
        for i in range(len(s)):
            new_s.append(s[i])
            new_s.append('')
        
        # '.'가 존재할 수 있는 위치 -> 홀수 인덱스
        for i, j, k in comb_list:
            s_copy = copy.deepcopy(new_s)
            s_copy[2*i+1] = '.'
            s_copy[2*j+1] = '.'
            s_copy[2*k+1] = '.'
            # 리스트를 스트링으로 합친다.
            ip = ''.join(s_copy)
            if is_valid(ip):
                result.append(ip)
                
        return result
