'''
[feedback]
- 메모리 초과 이유: while문 내부에서 무한 루프 진행 => 중복된 이름(이름 + 접미사)에 대해서 탐색 후에 같은 loop내에서 name_dictionary에 대해서 저장 진행
-> 문제: 탐색 후에 loop 밖에서 저장하지 않고 내부 loop 내에서 저장을 해버리니 -> 다음 탐색 정보도 저장되어서 무한루프에 빠짐 

- 추가적인 내용: 주석을 달아주세요.★★★★★

'''

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        used = {}
        output = []
        for i in names:
            if i not in used:
                used[i] = 1
                output.append(i)
            else:
                k = used[i]
                used[i] += 1
                new = i + "(" + str(k) + ")"
                                
                # 이전 코드 
                '''while new in used:
                    k += 1
                    new = i + "(" + str(k) + ")"
                    used[new] = 1
                    output.append(new)'''
                
                # 수정 코드 
                while new in used:
                    k += 1
                    new = i + "(" + str(k) + ")"
                used[new] = 1
                output.append(new)
                
        return(output)
    
#메모리 초과
