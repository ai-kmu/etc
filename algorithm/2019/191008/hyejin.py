def solution(tickets):
    answer = []
    #총 나라 수
    contry = len(tickets)
    trip ={}
    for path in tickets:
        if path[0] not in trip:
            trip[path[0]] = [path[1]]
        else :
            trip[path[0]].append(path[1])
            
    path = "ICN"
    answer.append(path)
    """
    문제 알파벳순서로 뽑다가 나머지 국가를 들리지 못한다. 그문제는 어떻게 해결할 것인가.
    => 그문제를 해결하기 위해서 코드를 고쳤지만, 테스트 케이스 1이 나오지 않음.
    나라를 들릴 때마다 -1을 하고, contry가 0이 될때까지 한다.
    """
    while contry > 0 :
        before_path = path
        if len(trip[path]) >= 1 :
            trip[path].sort()
            path = trip[path][0]
            for i in range(0,len(trip[before_path])):
                test_trip = trip[before_path][i]
                if trip.get(test_trip) == None :
                    continue
                if len(trip[test_trip]) == 1 and path not in trip[test_trip] : 
                    path = test_trip
                    break
            contry -= 1
            trip[before_path].remove(path)
            answer.append(path)
        if trip.get(path) == None:
            break
    return answer
