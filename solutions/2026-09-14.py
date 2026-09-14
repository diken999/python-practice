def rotate_ends(record: tuple) -> tuple:
    sid, *arr = record
    if len(arr) < 2:
        return (sid, *arr)
    else:
        first, *center, last = arr
    return (sid, last, *center, first)

def summarize(records) -> list:
    result = []
    records_map = {}
    for item in records:
        sid, *arr = item
        if sid in records_map:
           old_index = records_map[sid]
           old_item = result[old_index]
           count = len(arr) + old_item[1]
           total = sum(arr) + old_item[2]
           avg = round(total / count, 2)
           result[old_index] = (sid, count, total, avg)
        else :
            count = len(arr)
            total = sum(arr)
            avg = round(total / count, 2) if count != 0 else 0.0
            result.append((sid, count, total, avg))
            # TODO 踩坑
            records_map[sid] = len(result) - 1
    return result

if __name__ == '__main__':
    print(rotate_ends(("A", 1, 2, 3, 4)))
    print(rotate_ends(("A", 1, 2)))
    print(summarize([("A", 1, 2, 3, 4), ("B", 10), ("A", 5, 6)]))
