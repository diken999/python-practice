def make_intro(name: str, age: int, city: str) -> str:
    return f"我是{name.strip()}，今年{age}岁，来自{city.strip()}。"


if __name__ == "__main__":
    name = input("请输入名字 ")
    age = int(input("请输入年龄 "))
    city = input("请输入城市 ")
    print(make_intro(name, age, city))