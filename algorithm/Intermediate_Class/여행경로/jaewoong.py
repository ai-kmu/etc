#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#풀이 실패...
def solution(tickets):
    answer = []
    now = 'ICN'
    answer.append(now)
    
    def next_ticket(tickets,loc_now):
        max = ''
        for i in range(len(tickets)):
            if loc_now in tickets[i][0]:
                loc_now = tickets[i][1]
                print(loc_now)
        
    next_ticket(tickets,now)

    return answer

