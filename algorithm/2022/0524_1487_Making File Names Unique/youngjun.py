class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        dict = defaultdict(int)
        re_names = []

        for i in range(len(names)):
            if names[i] in dict:
                dict[names[i]] += 1
                if names[i].count('(') == 0:
                    new_name = names[i] + '(' + str(dict[names[i]]) + ')'
                    re_names.append(new_name)
                elif names[i].count('(') != 0:
                    new_name = names[i] + '(' + str(dict[names[i]]) + ')'
                    re_names.append(new_name)
            elif names[i] is not dict:
                dict[names[i]] += 1
                if names[i].count('(') == 0:
                    re_names.append(names[i])
                elif names[i].count('(') != 0:
                    ori_name = re.sub("[(]"," ", names[i])
                    ori_name = re.sub("[)]","", ori_name)
                    ori_num = ori_name.split(" ")[1]
                    ori_name = ori_name.split(" ")[0]
                    dict[ori_name] = int(ori_num)
                    re_names.append(names[i])

        return re_names
