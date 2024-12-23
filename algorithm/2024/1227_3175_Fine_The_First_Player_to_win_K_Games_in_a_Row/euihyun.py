# 실패~ 정답 봤수 아래는 틀린코드요

# from collections import deque

# class Solution(object):
#     def findWinningPlayer(self, skills, k):
#         """
#         :type skills: List[int]
#         :type k: int
#         :rtype: int
#         """
#         # 인덱스별 player가 가지고 있는 패, player의 순서는 맘대로 바꾸면 안됨
#         # 내 인덱스에서 다음놈이랑 전투하면 됨 
#         # k 번 연속으로 이기면 되고

#         mapping_list = skills
#         n = len(skills)
#         skills = deque(skills)
#         cnt = 0

        
#         if k == 1:
#             return mapping_list.index(max(skills[0], skills[1]))
        
#         if k >= n:
#             return mapping_list.index(max(skills))
        
#         for i in range(10**10):
#             for j in range(1):
#                 if skills[j] < skills[j+1]:
#                     cnt = 0
#                     temp = skills.popleft()
#                     skills.append(temp)
#                     cnt += 1

#                 cnt += 1
#                 if skills[j] > skills[j+1]:
#                     # [4,6,3,9,2]
#                     # [6,3,9,2,4]
                    
#                     temp = skills.popleft()
#                     insert_num = skills.popleft()
#                     skills.appendleft(temp)
#                     skills.append(insert_num)

                    
#                 if cnt == k:
#                     return(mapping_list.index(skills[0]))

# 졸라쉽게 풀수있었네..
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        
        champSkill, champion, tally = skills.pop(0), 0, 0

        for i, skill in enumerate(skills, start = 1):
            
            if skill > champSkill: 
                champion, champSkill, tally = i, skill, 0
                
            tally+= 1

            if tally == k: return champion
        
        return champion
        
