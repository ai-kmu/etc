'''
아래 주석 처리된 코드는 solution 코드 공부하면서 제 스타일로 바꾼 거예요.
근데, ddict보다는 Counter가 나을 거 같아서 Counter로 바꿔봤어요 (주석 밑에 코드)
알고리즘은 동일한데, Counter 객체끼리 더해서 업데이트가 가능하다는 게 가장 큰 차이점이에요
for문 쓰기가 싫었어요
설명은 Counter 버전에만 달았습니당
'''

# from collections import defaultdict as ddict

# class Solution:
#     def get_count(self, s: str, idx: int) -> str:
#         count = ""
#         while idx < len(s) and s[idx].isdigit():
#             count += s[idx]
#             idx += 1

#         count = int(count) if count else 1
#         return count, idx

#     def countOfAtoms(self, formula: str) -> str:
#         index = 0
#         stack = [ddict(int)]

#         while index < len(formula):
#             s = formula[index]
#             if s == "(":
#                 stack.append(ddict(int))
#                 index += 1
#             elif s == ")":
#                 count, index = self.get_count(formula, index + 1)
#                 curr_tmp = stack.pop()
#                 curr_tmp = {k: v * count for k, v in curr_tmp.items()}
#                 prev_tmp = stack[-1]
#                 for k, v in curr_tmp.items():
#                     prev_tmp[k] += v
#             elif s.isupper():
#                 index += 1
#                 atom = s
#                 while index < len(formula) and formula[index].islower():
#                     atom += formula[index]
#                     index += 1
                
#                 count, index = self.get_count(formula, index)
#                 prev_tmp = stack[-1]
#                 prev_tmp[atom] += count

#         sorted_tmp = sorted([f"{atom}" if count == 1 else f"{atom}{count}" for atom, count in stack[-1].items()])
#         return "".join(sorted_tmp)


from collections import Counter

class Solution:
    # 숫자 가져오는 함수
    def get_count(self, s: str, idx: int) -> str:
        count = ""
        while idx < len(s) and s[idx].isdigit():
            count += s[idx]
            idx += 1

        count = int(count) if count else 1
        return count, idx

    def countOfAtoms(self, formula: str) -> str:
        # 초기화
        index = 0
        stack = [Counter()]
        # index 돌면서 탐색
        while index < len(formula):
            s = formula[index]
            # 여는 괄호 : 새로 Counter 저장 -> 여기에 () 안의 내용이 들어감
            if s == "(":
                stack.append(Counter())
                index += 1
            # 닫는 괄호 : 괄호 뒤의 숫자 `count` 만큼 괄호 안의 Counter를 업데이트
            elif s == ")":
                # `count` 얻어서
                count, index = self.get_count(formula, index + 1)
                # 이번 괄호까지의 Counter 갖고 와서
                tmp = stack.pop()
                # `* count` 해주고
                tmp = Counter({k: v * count for k, v in tmp.items()})
                # 그전 Counter에다가 괄호 내용을 업데이트
                stack[-1] = tmp + stack[-1]  # !! ddict랑 요기가 다름
            # 대문자여야 시작 가능함
            elif s.isupper():
                # 소문자까지 해서 전체 다 가져오기
                index += 1
                atom = s
                while index < len(formula) and formula[index].islower():
                    atom += formula[index]
                    index += 1

                # `count` 가져와서 그전 Counter에다가 업데이트
                count, index = self.get_count(formula, index)
                stack[-1][atom] += count

        # sorting 해야됨
        # 근데 '1'은 생략해야되니까 if 문 처리
        sorted_tmp = sorted([f"{atom}" if count == 1 else f"{atom}{count}" for atom, count in stack[-1].items()])
        return "".join(sorted_tmp)
