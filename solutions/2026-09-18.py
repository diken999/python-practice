def parse_record(item: str) -> tuple[str, float]:
    if item.count(":") != 1:
        raise FormatError('格式错误')
    name, score_str = item.split(':', 1)
    name = name.strip()
    score_str = score_str.strip()
    if name == "" or score_str == "":
        raise FormatError('格式错误')
    try:
        score = float(score_str)
    except ValueError as e:
        raise FormatError('格式错误') from e
    if score < 0 or score > 100:
        raise RangeError('分数超范围')
    return name, score


def import_scores(lines: list[str], strict: bool = False) -> tuple[dict[str, float], list[tuple[int, str]]]:
    result = {}
    fail_list = []
    if len(lines) == 0:
        raise ScoreImportError
    for idx, item in enumerate(lines):
        try:
            name, score = parse_record(item)
            if name in result:
                raise DuplicateError('姓名重复')
            result[name] = score

        except ScoreImportError as e:
            if strict == True:
                raise
            else:
                fail_list.append((idx + 1, str(e)))
                continue

    return (result, fail_list)
    

class ScoreImportError(Exception):
    """分数导入的基础异常"""
    pass
class FormatError(ScoreImportError):
    """数据格式错误"""
    pass
class RangeError(ScoreImportError):
    """分数超出合理范围"""
    pass
class DuplicateError(ScoreImportError):
    """存在重复分数记录"""
    pass


if __name__ == "__main__":
    lines = [
    "小明:88",       # 1 正常
    " 小红 : 92.5 ", # 2 正常(姓名与分数两端空白应被忽略)
    "小明:70",       # 3 姓名重复
    "小李",          # 4 格式错误(没有冒号)
    "小张:",         # 5 格式错误(分数为空)
    ":80",           # 6 格式错误(姓名为空)
    "小王:120",      # 7 分数超范围
    "小赵:-5",       # 8 分数超范围
    "小钱:0",        # 9 正常(下边界)
    "小孙:100",      # 10 正常(上边界)
    ]
    scores, fail = import_scores(lines)
    print(scores)
    print(fail)