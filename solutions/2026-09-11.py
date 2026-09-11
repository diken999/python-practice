# 洗一次牌
def shuffle_once(nums: list) -> list:
    odd_pos =  nums[1::2]
    even_pos = nums[::2]
    return even_pos + odd_pos

def is_same(nums_1: list, nums_2: list) -> bool:
    flag = True
    if len(nums_1) != len(nums_2):
        return False
    for idx, it in enumerate(nums_1):
        if it != nums_2[idx]:
            flag = False
    return flag

def min_steps(nums: list) -> int:
    steps = 1
    shuffle_list = shuffle_once(nums)
    while is_same(nums, shuffle_list) == False:
        shuffle_list = shuffle_once(shuffle_list)
        steps += 1
    return steps

if __name__ == "__main__":
    print(shuffle_once([1, 2, 3, 4, 5, 6])) # [1, 3, 5, 2, 4, 6]

    # 2) 长度为 4: [1,2,3,4] -> [1,3,2,4] -> [1,2,3,4]
    print(min_steps([1, 2, 3, 4]))            # 2

    # 3) 边界: 长度为 1 / 2
    print(min_steps([7]))                   # 1  (洗一次还是 [7])
    print(min_steps([1, 2]))                  # 1  (洗一次就变回 [1,2])

    # 4) 长度为 3 / 5 / 6
    print(min_steps([1, 2, 3]))               # 2
    print(min_steps([1, 2, 3, 4, 5]))         # 4
    print(min_steps([1, 2, 3, 4, 5, 6]))      # 4

    # 5) 陷阱: 元素有重复值, 不能用集合/排序后的结果比较
    print(min_steps([1, 1, 2, 2]))
