max_price = 1001


# 재귀 이용해서 풀기 (시간 초과)
def paint_house(house_index, color_index, first_color_index):
    global price_of_house, num_house
    if house_index == num_house-1:
        if first_color_index == color_index:
            return max_price
        else:
            return price_of_house[house_index][color_index]
    return min(price_of_house[house_index][color_index]
               + paint_house(house_index + 1, (color_index + 1) % 3, first_color_index),
               price_of_house[house_index][color_index]
               + paint_house(house_index + 1, (color_index + 2) % 3, first_color_index))


# Input
num_house = int(input())
price_of_house = [list(map(int, input().split())) for _ in range(num_house)]
answer = min(paint_house(0, 0, 0), paint_house(0, 1, 1), paint_house(0, 2, 2))
print(answer)

