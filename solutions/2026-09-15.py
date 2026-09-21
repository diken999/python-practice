def flatten(d: dict, sep: str = ".") -> dict:
    """把嵌套 dict 打平成单层 dict，sep 连接路径各段。"""
    result = {}
    def flatten_dict(current_dict: dict, current_path: str):
        for k, v in current_dict.items():
            current_path = k if current_path == "" else current_path + sep + k
            if isinstance(v, dict) and len(v) > 0:
                result[current_path] = flatten_dict(v, current_path)
            else:
                result[current_path] = v
        pass
    for k, v in d.items():
        if isinstance(v, dict) and len(v) > 0:
           flatten_dict(v, "")
        else:
            result[k] = v
    return result

def unflatten(flat: dict,  sep: str = ".") -> dict:
    """把 flatten 的结果还原成嵌套 dict。"""
    result = {}
    def unflatten_dict(key_arr: list, value):
        temp_dict = result
        for idx, key in enumerate(key_arr):
            if key in temp_dict:
                temp_dict = temp_dict[key]
                continue
            if idx != len(key_arr) - 1:
                temp_dict[key] = {}
                temp_dict = temp_dict[key]
            else:
                temp_dict[key] = value

    for k, v in flat.items():
        key_list = k.split(sep)
        if len(key_list) > 1:
            unflatten_dict(key_list, v)
        else:
            result[k] = v
    return result


if __name__ == "__main__":
    print(unflatten({"a.b": 1, "a.c.d": 2, "e": 3}))
    print(unflatten({"x": {}, "y.z": {}}))
    print(unflatten({"a_list.0.name": "tom", "a_list.1.name": "amy"}, sep="."))
