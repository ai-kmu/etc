# runtime Error 해결 방법: 정답에 같은 값 확인할 떄 => list 대신 dictionary key로 활용
# list => O(n) / dictionary => O(1) 
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        name_cnt = {}
        answer = []
        for name in names:
            # 처음 본 이름이라면 정답에 추가하고 dict에 값을 1로 생성
            if name not in name_cnt:
                name_cnt[name] = 1
                answer.append(name)
            else:
                # 이미 있는 값이라면
                cnt = name_cnt[name]
                temp = name + '(' + str(cnt) + ')'
                # 정답에 같은게 없을때까지 숫자를 늘려줌
                while temp in name_cnt
                #while temp in answer:
                    cnt += 1
                    temp = name + '(' + str(cnt) + ')'
                name_cnt[name] = cnt
                # 생성한 temp도 dict에 추가
                name_cnt[temp] = 1
                answer.append(temp)
        return answer
