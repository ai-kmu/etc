'''
입력: ["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]
내 출력: ["kaido","kaido(1)","kaido(2)","kaido(1)(1)","kaido(2)"]
정답 출력: ["kaido","kaido(1)","kaido(2)","kaido(1)(1)","kaido(2)(1)"]

이 Testcase에서 걸림...... 수정 필요함......
'''


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        # {name: name이 몇 번 나왔는지}를 저장하는 dict
        dict = defaultdict(int)
        # 출력 리스트 초기화
        re_names = []

        for i in range(len(names)):
            if names[i] in dict:
                # 중복되어 들어가는 경우 key의 value를 1씩 더함
                dict[names[i]] += 1
                # 괄호가 없는 경우, 들어간 name에 괄호를 더하고, dict의 키를 추가한다.
                if names[i].count('(') == 0:
                    new_name = names[i] + '(' + str(dict[names[i]]) + ')'
                    re_names.append(new_name)
                elif names[i].count('(') != 0:
                    new_name = names[i] + '(' + str(dict[names[i]]) + ')'
                    re_names.append(new_name)
            elif names[i] is not dict:
                # 새로 들어가는 경우 name을 key로 넣어주고 0으로 초기화 
                dict[names[i]] = 0
                # 괄호가 없는 경우 리스트에 추가
                if names[i].count('(') == 0:
                    re_names.append(names[i])
                # 괄호가 있는 경우, 괄호를 벗겨낸 name을 key로 넣어주고 괄호 속 숫자를 value로 설정, name을 리스트에 추가한다.
                elif names[i].count('(') != 0:
                    ori_name = re.sub("[(]"," ", names[i])
                    ori_name = re.sub("[)]","", ori_name)
                    ori_num = ori_name.split(" ")[1]
                    ori_name = ori_name.split(" ")[0]
                    dict[ori_name] = int(ori_num)
                    re_names.append(names[i])

        return re_names
