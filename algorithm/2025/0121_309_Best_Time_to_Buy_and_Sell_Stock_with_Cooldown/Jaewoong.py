def maxProfit(self, prices: List[int]) -> int:
    # buy: 주식을 구매했을 때의 최대 이익 (주식을 보유하고 있을 때의 상태)
    # sell: 주식을 팔았을 때의 최대 이익 (주식을 팔고 난 후 상태)
    # rest: 아무것도 하지 않고 대기하는 상태에서의 최대 이익
    buy, sell, rest = -prices[0], 0, 0  # 초기값 설정: 첫 번째 날 주식을 사는 경우 buy = -prices[0], 팔지 않은 상태 sell = 0, 아무것도 하지 않는 상태 rest = 0

    # prices 배열을 순차적으로 처리
    for price in prices:
        # 한 줄로 update를 처리하여 잘못된 순서로 값이 업데이트되는 것을 방지
        buy, sell, rest = (
            max(rest - price, buy),  # buy는 이전에 아무것도 하지 않다가 주식을 새로 사는 경우(rest - price)와 이전에 주식을 샀던 상태(buy)의 최대값
            max(buy + price, sell),  # sell은 주식을 팔아서 얻는 이익(buy + price)과 팔지 않은 상태에서의 최대 이익(sell)의 최대값
            sell                      # rest는 팔고 난 후 아무것도 하지 않는 상태(sell)를 그대로 유지
        )

    # 최종적으로 주식을 팔았을 때의 최대 이익을 반환 (sell 상태에서 얻을 수 있는 이익)
    return sell  # 또는 max(buy, sell, rest)로 반환 가능, 여기서는 sell 값이 최대 이익을 나타냄
