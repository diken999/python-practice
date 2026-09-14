def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if len(intervals) == 0:
        return []
    ordered = sorted(intervals, key = lambda x: x[0])
    result_list = [[ordered[0][0], ordered[0][1]]]
    for item in ordered:
        last_item = result_list[-1]
        if item[0] <= last_item[1]:
            result_list[-1] = [min(item[0], last_item[0]), max([item[1], last_item[1]])]
        else:
            result_list.append([*item])
    return result_list

if __name__ == "__main__":
    print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(merge_intervals([[1, 4], [4, 5]]))
    print(merge_intervals([[1, 10], [2, 3], [4, 8]]))
    print(merge_intervals([]))
    print(merge_intervals([[5, 6], [1, 3]]))
    print(merge_intervals([[1, 1], [1, 2], [3, 3]]))
