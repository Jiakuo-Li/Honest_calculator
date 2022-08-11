# write your code here
operation_list = ["+", "-", "*", "/"]
memory = float(0)
msg_list = ["Enter an equation",
            "Do you even know what numbers are? Stay focused!",
            "Yeah... division by zero. Smart move...",
            "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
            "Do you want to store the result? (y / n):",
            "Do you want to continue calculations? (y / n):",
            "",
            "",
            "",
            "",
            "Are you sure? It is only one digit! (y / n)",
            "Don't be silly! It's just one number! Add to the memory? (y / n)",
            "Last chance! Do you really want to embarrass yourself? (y / n)"]


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += " ... lazy"
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += " ... very lazy"
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += " ... very, very lazy"
    if msg != "":
        msg = "You are" + msg
        print(msg)


while True:
    user_input = input(msg_list[0])
    x, oper, y = user_input.split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        x = float(x)
        y = float(y)
    except Exception:
        print(msg_list[1])
        continue
    else:
        if oper in operation_list:
            check(x, y, oper)
            if oper == "+":
                result = x + y
            elif oper == "-":
                result = x - y
            elif oper == "*":
                result = x * y
            elif oper == "/" and y != 0:
                result = x / y
            elif oper == "/" and y == 0:
                print(msg_list[2])
                continue
        else:
            print(msg_list[3])
            continue
    print(result)
    while True:
        store = input(msg_list[4])
        if store == "y":
            if is_one_digit(result):
                msg_index = 10
                while True:
                    answer = input(msg_list[msg_index])
                    if answer == "y" and msg_index < 12:
                        msg_index += 1
                        continue
                    elif answer == "y" and msg_index >= 12:
                        memory = result
                        break
                    elif answer != "y" and answer != "n":
                        continue
                    elif answer == "n":
                        break
                break
            else:
                memory = result
                break
        elif store == "n":
            break
        else:
            continue
    while True:
        continue_ = input(msg_list[5])
        if continue_ != "y" and continue_ != "n":
            continue
        else:
            break
    if continue_ == "y":
        continue
    elif continue_ == "n":
        break
