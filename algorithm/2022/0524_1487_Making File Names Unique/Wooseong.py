from collections import defaultdict

class Solution:
    def getFolderNames(self, names):
        # 현재까지 들어온 name의 개수를 센다
        count = defaultdict(int)
        answer = []
        for name in names:
            # 들어온적이 있었다면
            if count[name] > 0:
                # 가능한 숫자를 탐색한다
                while f'{name}({count[name]})' in count:
                    count[name] += 1

                new_name = f'{name}({count[name]})'
                # 가능한 걸로 answer에 넣고
                answer.append(new_name)
                # answer에 넣은 것에 대해서도 count한다
                count[new_name] += 1

            # 들어온 적 없으면
            else:
                # answer에 넣는다
                answer.append(name)

            # input으로 들어온 name에 대해서는 어떤 경우든 count해줘야 한다
            count[name] += 1
        return answer
