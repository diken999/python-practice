def calc_tax(income: int) -> int:
    tax_money = income - 5000
    if tax_money <= 0:
        return 0
    elif tax_money <= 3000:
        return int(tax_money * 3 // 100)
    elif tax_money <= 12000:
        return int(tax_money * 10 // 100 - 210)
    elif tax_money <= 25000:
        return int(tax_money * 20 // 100 - 1410)
    elif tax_money <= 35000:
        return int(tax_money * 25 // 100 -2660)
    elif tax_money <= 55000:
        return int(tax_money * 30 // 100 - 4410)
    elif tax_money <= 80000:
        return int(tax_money * 35 // 100 - 7160)
    else:
        return int(tax_money * 45 // 100 - 15160)

if __name__ == '__main__':
    money = int(input())
    print(calc_tax(money))
