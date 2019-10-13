def solution(tickets):
    answer = []
    #총 나라 수
#     contry = len(tickets)
#     trip ={}
#     for path in tickets:
#         if path[0] not in trip:
#             trip[path[0]] = [path[1]]
#         else :
#             trip[path[0]].append(path[1])
            
#     path = "ICN"
#     answer.append(path)
#     """
#     문제 알파벳순서로 뽑다가 나머지 국가를 들리지 못한다. 그문제는 어떻게 해결할 것인가.
#     => 그문제를 해결하기 위해서 코드를 고쳤지만, 테스트 케이스 1이 나오지 않음.
#     나라를 들릴 때마다 -1을 하고, contry가 0이 될때까지 한다.
#     """
    # while contry > 0 :
    #     before_path = path
    #     if len(trip[path]) >= 1 :
    #         trip[path].sort()
    #         path = trip[path][0]
    #         for i in range(0,len(trip[before_path])):
    #             test_trip = trip[before_path][i]
    #             if trip.get(test_trip) == None :
    #                 continue
    #             if len(trip[test_trip]) == 1 and path not in trip[test_trip] : 
    #                 path = test_trip
    #                 break
    #         contry -= 1
    #         trip[before_path].remove(path)
    #         answer.append(path)
    #     if trip.get(path) == None:
    #         break
    
    
    '''2번째 방법, 2차원 배열로 만들어서 각 나라가 연결되어 있으면, 1 아니면, 0으로 해놓는다. 그러면 어떤 노드가 연결되어 있는지        알 수 있는 map이 생기는 것이고, ICN부터 시작하여 각 나라들을 방문하는데 알파벳 순서대로 방문을 한다. 하지만 알파벳순서로       방문을 하게 되면, 다시 돌아갈 수 있는 경로가 없는 경우까지 계산을 해야한다. 방문하면서 answer에 방문한 나라를 저장하고  
       len(tickets)+1이 되면 다 돈것이니 그만한다.
    '''
    return answer
