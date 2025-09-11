prices = [7,6,4,3,1]
class Solution(object):
    def maxProfit(self, prices):
        smallest = min(prices)
        last_ele = len(prices) - 1
        smallest_ele_index = prices.index(smallest)
        max_val = []
        if smallest_ele_index == len(prices) - 1:
            return 0
        else:
            for i in range(smallest_ele_index, last_ele):
                    if prices[i] > smallest:
                        max_val.append(prices[i])
        max_ele = max(max_val)
        result = max_ele - smallest
        return result


print(float('inf') + 10000)