from itertools import combinations
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # valid ip address 찾기
        # 각 자리마다 255를 넘지 말아야함
        # 가능한 .의 배치를 모두 구함
        # valid한 ip를 걸러냄
        # n-1C3의 조합을 모두 탐색
        
        n = len(s)
        combi = combinations(range(1, n), 3)
        answer = []
        for pair in combi:
            i, j, k = pair
            ip = [s[:i], s[i:j], s[j:k], s[k:]]
            str_ip = f'{s[:i]}.{s[i:j]}.{s[j:k]}.{s[k:]}'
            flag = True # ip가 valid한지 안한지
            for sub_ip in ip: # 각 ip 조건 탐색
                if int(sub_ip) > 255 or (sub_ip[0] == '0' and len(sub_ip) > 1):
                    flag = False
                    break
            if flag: # valid하면 추가
                answer.append(str_ip)
                                                                      
        return answer
