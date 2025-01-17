class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    # sell: 주식을 팔고 난 후 최대 이익 (현재까지 팔았을 때의 최대 이익)
    # hold: 주식을 가지고 있는 상태에서 최대 이익 (현재까지 주식을 가지고 있는 상태에서 얻은 최대 이익)
    # prev: 이전에 주식을 팔았을 때의 최대 이익 (sell의 이전 값을 저장)
    sell = 0
    hold = -math.inf  # 초기값을 -무한대로 설정하여 주식 구매를 허용
    prev = 0

    # 주어진 가격 배열을 순차적으로 처리
    for price in prices:
      # 현재 sell 값을 cache에 저장해두어 hold 계산에서 사용
      cache = sell
      # sell 값 업데이트: 현재까지의 sell 값과, 주식을 팔았을 때 얻을 수 있는 최대 이익을 비교
      # hold + price: 주식을 보유하고 있었던 상태에서 현재 가격에 팔았을 때 얻을 수 있는 이익
      sell = max(sell, hold + price)
      # hold 값 업데이트: 주식을 가지고 있는 상태에서 얻을 수 있는 최대 이익을 비교
      # prev - price: 이전에 팔았을 때의 최대 이익에서 현재 가격을 뺀 값 (즉, 주식을 새로 사고 보유하는 이익)
      hold = max(hold, prev - price)
      # prev 값은 현재 sell 값으로 갱신하여 다음 번에 사용할 수 있도록 함
      prev = cache

    # 최종적으로 팔았을 때의 최대 이익을 반환
    return sell
