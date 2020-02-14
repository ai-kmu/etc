# 재귀 이용해서 풀기 (시간 초과)
# def paint_house(house_index, color_index, first_color_index):
#     global price_of_house, num_house
#     if house_index == num_house-1:
#         if first_color_index == color_index:
#             return max_price
#         else:
#             return price_of_house[house_index][color_index]
#     return min(price_of_house[house_index][color_index]
#                + paint_house(house_index + 1, (color_index + 1) % 3, first_color_index),
#                price_of_house[house_index][color_index]
#                + paint_house(house_index + 1, (color_index + 2) % 3, first_color_index))


# Input
# number of house
num_house = int(input())
# max값
max_price = 1001 * num_house
# 각 house color의 price
price_of_house = [list(map(int, input().split())) for _ in range(num_house)]
# answer = min(paint_house(0, 0, 0), paint_house(0, 1, 1), paint_house(0, 2, 2))
# print(answer)

# n번째까지의 price sum
sum_of_house = [[-1]*3 for _ in range(num_house)]

# 처음은 아무거나 큰값
answer = max_price

for i in range(3):
    # 첫번째 house 색깔 고정
    # 첫번째와 마지막의 색깔 겹침 문제 때문
    sum_of_house[0][i] = price_of_house[0][i]
    sum_of_house[0][(i+1)%3] = max_price
    sum_of_house[0][(i+2)%3] = max_price

    for house_index in range(1, num_house):
        sum_of_house[house_index][0] = min(sum_of_house[house_index-1][1] + price_of_house[house_index][0],
                                           sum_of_house[house_index-1][2] + price_of_house[house_index][0])

        sum_of_house[house_index][1] = min(sum_of_house[house_index - 1][0] + price_of_house[house_index][1],
                                           sum_of_house[house_index - 1][2] + price_of_house[house_index][1])

        sum_of_house[house_index][2] = min(sum_of_house[house_index - 1][0] + price_of_house[house_index][2],
                                           sum_of_house[house_index - 1][1] + price_of_house[house_index][2])
    sum_of_house[num_house-1][i] = max_price
    sum_min = min(sum_of_house[num_house-1])
    answer = min(sum_min, answer)

# 예외 house가 1개일 때.
if num_house == 1:
    answer = min(price_of_house[0])

print(answer)
