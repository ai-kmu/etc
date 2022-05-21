# 28 / 33 test cases passed.
# 시간 초과..

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        # 정답 리스트 생성
        ans = []
        
        #i에 names 하나씩 지정 
        for i in names:
            # ans에 없으면 추가
            if i not in ans:
                ans.append(i)
            # ans 에 있는경우 중복되는 수 체크해서 중복되는 문자+count 해서 추가해줌
            else:
                # 중복되는 경우니까 1부터 시작
                count = 1
                while True:
                    # gta(count)만들고 gta(count)가 있다면 (2)를 생성 
                    temp = str(i + "({})".format(count))
                    if temp in ans:
                        count += 1
                    # 없는 경우 정답에 추가
                    else:
                        ans.append(temp)
                        break
        return ans
        
