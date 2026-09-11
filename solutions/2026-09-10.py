def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if len(intervals) == 0:
        return []
    ordered = sorted(intervals, key = lambda x: x[0])
    result_list = [ordered[0][0], ordered[0][1]]
    for item in intervals:
        is_in_list = False
        for res_index, res_item in enumerate(result_list):
            if item[0] >= res_item[0] and item[1] <= res_item[1]:
                is_in_list = True
                break
            if item[1] < res_item[0] or item[0] > res_item[1]:
                continue
            if item[0] >= res_item[0] or item[1] <= res_item[1]:
                result_list[res_index] = [min(item[0], res_item[0]), max(item[1], res_item[1])]
                is_in_list = True
                break
        if is_in_list == False:
            result_list.append(item)
    # result_list.sort(key = lambda x: x[0])
    # return result_list
    return sorted(result_list, key=lambda x: x[0])

if __name__ == "__main__":
    print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(merge_intervals([[1, 4], [4, 5]]))
    print(merge_intervals([[1, 10], [2, 3], [4, 8]]))
    print(merge_intervals([]))
    print(merge_intervals([[5, 6], [1, 3]]))
    print(merge_intervals([[1, 1], [1, 2], [3, 3]]))
