#Coin Change


class Solution(object):
    def coinChange(self, coins, amount):
        #amount+1만큼 크기의 리스트 생성
        case_list = [0 for i in range(amount+1)]
        #각 금액을 만들수 있는 경우의 수 구하기

        for i in range(1, amount + 1):
            if i in coins: #자기 자신 채우기
                case_list[i] = 1
                continue

            min_coins = float("inf") # 양의 무한대

            for coin in coins:
                if i - coin >= 0:
                    min_coins = min(case_list[i - coin], min_coins) # 최소 동전 개수 계산
            case_list[i] = min_coins + 1

        #-1인 경우에 대한 예외 처리
        if case_list[len(case_list)-1] == float("inf"):
            return -1
        else:
            return case_list[len(case_list)-1]

if __name__ == '__main__':
    coins=[5,2,1]
    amount=11
    s=Solution()
    print(s.coinChange(coins,amount))