#6:20~ 7:00
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        remainedRoomsNum=len(rooms)
        remainedRooms=[False for i in range(len(rooms))]
        acquiredKeys=[False for i in range(len(rooms))]
        
        #첫번째 room 방문 
        for i in rooms[0]:
            acquiredKeys[i]=True
        remainedRooms[0]=True
        remainedRoomsNum-=1
        
        #room을 방문하면서 더이상 방문한 room이 줄어들지 않거나 다 줄어들 때 까지 반복 
        while True:
            
            for idx,val in enumerate(remainedRooms):
                if not val:
                    if acquiredKeys[idx]:
                        remainedRooms[idx]=True
                        for key in rooms[idx]:
                            acquiredKeys[key]=True
            
            #이전과 현재 남아있는 room 개수 비교 
            curRemainedRoomsNum=remainedRooms.count(False)
            if remainedRoomsNum==curRemainedRoomsNum: # 이전과 다르지 않다면 더이상 방문못하기 때문에 break
                break
            else:
                remainedRoomsNum=curRemainedRoomsNum 
                        
        return remainedRoomsNum==0
        
        
            
        
       
    
    
        
            
            
                
        
        
