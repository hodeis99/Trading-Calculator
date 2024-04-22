import sys


def main():
    global buy_commission
    buy_commission = commission_questions("buy")
    global sell_commission
    sell_commission = commission_questions("sell")
    profit_loss = calculate(questions("buy"))
    if profit_loss > 0:
        print(f"You made a profit of {convert_number(profit_loss)}$")
    elif profit_loss < 0:
        print(f"You made a loss of {convert_number(profit_loss)}$")
    else:
        print(f"You broke even!")


def commission_questions(mood):
    mistake = 0
    if mood == "buy" or mood == "sell":
        commission = f"What is the {mood} commission percentage \
of your exchange? "
    else:
        raise ValueError
    while True:
        try:
            percent = float(input(commission))
            if not 0 <= percent <= 2:
                raise ValueError
        except:
            print("Wrong entry!")
            mistake += 1
            if mistake == 3:
                sys.exit()
        else:
            break

    return percent


def commission(price, amount, commission_percent):
    return price * amount * commission_percent / 100


def questions(mood):
    datas = []
    if mood == "buy" or mood == "sell":
        data_list = [f"{mood.title()} Price (in dollar): ",
                     f"{mood.title()} Amount: "]
    else:
        raise ValueError
    for i in data_list:
        mistake = 0
        while True:
            try:
                number = float(input(i))
            except:
                print("Wrong entry!")
                mistake += 1
                if mistake == 3:
                    sys.exit()
            else:
                break
        datas.append(number)
    return datas


def how_much(data, mood):
    price, amount = data
    if mood == "buy":
        return ((price * amount) - commission(price, amount, buy_commission)) * -1
    elif mood == "sell":
        return (price * amount) - commission(price, amount, sell_commission)
    else:
        raise ValueError


def calculate(first_buy):
    amount = first_buy[1]
    cal = [how_much(first_buy, "buy")]
    num = 0
    sell = 0
    while True:
        if amount == 0:
            return sum(cal)
        elif amount > 0:
            while True:
                next = input("Next step (Buy/Sell/Stop): ").lower()
                if next in ("buy", "sell"):
                    data = questions(next)
                    amount += data[1] if next == "buy" else -data[1]
                    cal.append(how_much(data, next))
                    sell += 1 if next == "sell" else 0
                    break
                elif next == "stop":
                    cal.append(how_much(first_buy, "buy") * -1)
                    if len(cal) == 2:
                        remain = 0
                    elif sell == 0:
                        remain = 0
                        cal.clear()
                    else:
                        remain = ((data[1] - amount) * data[0]) - \
                            commission(data[0], data[1], buy_commission) * -1
                    cal.append(remain)
                    return sum(cal)
                else:
                    print("Wrong entry!")
                    num += 1
                    if num == 3:
                        sys.exit()
        else:
            sys.exit("Wrong amounts!")


def convert_number(num):
    return int(num) if num.is_integer() else f"{num:.2f}"


if __name__ == "__main__":
    main()