# -*- coding: utf-8 -*-
"""Untitled17.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YleKifvIvIpXkr1CGPR5WuBh7tyKQeA9
"""

import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    
    while scoville[0] < K and len(scoville)>=1:
        if len(scoville) == 1:
            return -1
            
        now = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        answer = answer +1
        heapq.heappush(scoville, now)

        
    
    return answer