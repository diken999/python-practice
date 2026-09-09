def compress(s: str) -> str:
    result = ""
    index = 0
    while index < len(s):
        count = 1
        while index < len(s) - 1 and s[index] == s[index + 1]:
            count += 1
            index += 1
        result += s[index] + str(count)
        index += 1
    return result if len(result) < len(s) else s

if __name__ == "__main__":
    input_string = input()
    print(compress(input_string))
