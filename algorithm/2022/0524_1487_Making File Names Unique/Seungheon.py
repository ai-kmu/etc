class Solution(object):
    def getFolderNames(self, names):
        
        answer = [] 
        name_dict = defaultdict(list)

        # suffix가 있는지 확인
        def check_suffix(name):
            suffix_check = 0
            for i in range(len(name)-1, 1, -1):
                if(suffix_check == 0 and name[-1] == ')'):
                    suffix_check += 1
                # 접미사가 있는경우
                if(suffix_check == 1 and name[i] == '('):
                    suffix_check += 1
                    return name[i+1:-1] 
            return False
        
        # name을 사용할 수 있는지 확인
        def can_use_name(name):
            if 0 == len(name_dict[name]):
                return True
            return False
        
        # suffix 추가
        def add_suffix(name):
            num = 1
            while 1:
                new_name = name + '(' + str(num) + ')'
                if can_use_name(new_name):
                    name_dict[new_name].append(0)
                    answer.append(new_name)
                    break
                num+=1
                
        # suffix가 있는지 없는지 확인
            # suffix가 있으면 
                #r그대로 사용할 수 있는지 확인(name중에 있는 지확인)
                    # 사용할 수 있으면 사용
                        # dictionary에 0으로 추가
                        # dictionary 접미사를 땐 key에 suffix 추가
                    # 사용할수 없으면 suffix를 사용할 수 있을떄까지 수를 높여가며 붙임
                        # dictionary에 사용한 수 추가
            # suffix가 없으면
                # 사용할 수 있는지 확인
                    # 사용할 수 있으면 사용
                        # dictionary에 추가 0으로 추가
                    # 사용할 수 없으면 suffix를 사용할 수 있을때까지 수를 높여가며 붙임
                        # dictionary에 사용한 수 추가

        for name in names:
            if check_suffix(name):
                # 사용할 수 있으면 0추가하고 사용
                if can_use_name(name):
                    name_dict[name].append(0)
                    answer.append(name)
                else:
                    add_suffix(name)
            else:
                if can_use_name(name):
                    name_dict[name].append(0)
                    answer.append(name)
                else:
                    add_suffix(name)  
            
        return answer
