#엄청 긴 케이스에서 시간초과
from collections import defaultdict
class Solution:
    # dictionary를 사용해서 폴더 이름들의 개수를 센 후 2개 즉 겹치는것이 있으면
    # 조건에 맞는 폴더 이름 생성
    def getFolderNames(self, names: List[str]) -> List[str]:
        names_dict = defaultdict(int)
        for i in range(len(names)):
            names_dict[names[i]] += 1
            if names_dict[names[i]] != 1: # 이름이 겹칠 때
                index = 1 # 폴더이름 괄호 안에 들어갈 숫자
                while(1):
                    # 폴더 이름 생성
                    foldername = names[i] + '(' + str(index) +')'
                    # 만약 생성한 폴더가 names 안에 있고 폴더이름의 value값이
                    # 0이 아니라면 즉 앞에서 이미 개수를 셌다면
                    # index 값을 올려준다
                    if foldername in names and names_dict[foldername] != 0:
                        index += 1
                    
                    # 그게 아니라면 이름을 바꿨으니 겹치는 수를 빼고
                    # 폴더이름을 names 안에 넣어주고 폴더 이름에 대한 dictionay도 추가한다
                    else:
                        names_dict[names[i]] -= 1
                        names = names[:i] + names[i+1:]
                        names.insert(i, foldername)
                        names_dict[foldername] += 1
                        break
        
        return names
