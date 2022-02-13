class Solution(object):
    def totalFruit(self, fruits):
        """

        과일 2개를 담을 수 있는 최초의 위치를 찾아서 현재 위치와의 차를 구하여 가장 많이 담을 수 있는 수를 구한다

        dictionary를 만들어 과일을 하나씩 추가해가며 담은 과일의 종류가 3개가 되면
        담은 순서대로 제외시켜가며 과일이 2종류가되는 위치를 구한다
        (현재위치 - 과일의 종류가 2개가 되게하는 위치 +1 )를 하게되면 과일 2종류일때 basket에 담은 과일의 개수가 된다 

        """
        dic = defaultdict(int)
        startIdx = 0
        answer = []
        
        # 과일 목록에서 과일의 종류와 index를 가져온다
        for idx, fruit in enumerate(fruits):  
            # 과일을 앞에서부터 순서대로 basket에 담는다
            dic[fruit] += 1
            # 현재 담고있는 과일의 종류의 수가 3개가 되면 2개가 되게하는 처음위치를 구한다
            while len(dic) == 3 :
                # 처음위치를 구하기위해 순서대로 앞에서부터 담은 과일을 제거한다
                dic[fruits[startIdx]] -= 1
                # 과일의 개수가 0개가 되면 dictionary에서 제거한다
                if dic[fruits[startIdx]] == 0:
                    del dic[fruits[startIdx]]
                startIdx += 1
            # 과일의 종류가 2개일떄 담을 수 있는 개수의 값을 정답list에 추가 한다
            answer.append(idx - startIdx + 1)
        return max(answer)
