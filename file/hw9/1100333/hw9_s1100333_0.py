def homework_9(bag_size, items):
    def maxValue(bag_size, index, total_value):
        if bag_size == 0:
            return total_value
        if index == len(items):
            return total_value

        item = items[index]
        # 嘗試不拿當前物品的方案
        value1 = maxValue(bag_size, index + 1, total_value)
        # 嘗試拿當前物品的方案
        value2 = 0
        if item[0] <= bag_size:
            value2 = maxValue(bag_size - item[0], index + 1, total_value + item[1])
        return max(value1, value2)

    return maxValue(bag_size, 0, 0)
    