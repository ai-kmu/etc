class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # brute force: 모든 점에서 출발해서 모든 경우의 수를 구한 후 최댓갑 구하기 => O(n^2)
        # O(n)으로 풀어야 효율적으로 풀 수 있음 => backtracking을 막아야 함
        # 0번째부터 시작해서 앞으로 가다가 새로운 과일을 3개 이상 만나는 순간 멈춰야 함
        # 다만, 과거의 경로를 기록해두지 않으면 1번째부터 다시 시작해야함
        # 과거의 경로 중 알아야 하는 것만 기록해두면 0번째부터 시작해서 멈춘 순간 다시 돌아가지 않고 쭉 이어서 실행할 수 있다.
        # 제일 최근의 과일, 해당 과일이 연속적으로 몇번 이어져왔는지 알면
        # 해당 과일과 새로 마주친 과일을 담는 것으로 여기고 이어나가면 된다.
        answer = 0
        
        baskets = dict()
        previous_fruit = -1
        previous_fruit_num = 0
        
        for fruit in fruits:
            # 새로운 과일을 만남
            if len(baskets.items()) == 2 and fruit not in baskets.keys():
                # 직전 과일과 새로운 과일로 baskets을 새로 생성
                baskets = {
                    previous_fruit: previous_fruit_num,
                    fruit: 1
                }
                previous_fruit = fruit
                previous_fruit_num = 1
            else:
                # 그렇지 않을 경우 과일을 바구니에 담음
                baskets[fruit] = baskets.get(fruit, 0) + 1
                # 다만 직전 과일과 해당 과일이 얼만큼 이어져왔는지를 기록해 둠
                if fruit == previous_fruit:
                    previous_fruit_num += 1
                else:
                    previous_fruit = fruit
                    previous_fruit_num = 1
            
            answer = max(answer, sum(baskets.values()))
        return answer
