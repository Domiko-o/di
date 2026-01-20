print("Калькулятор")


a = float(input("Первое число: "))
b = float(input("Второе число: "))


print("Выбери операцию: +, -, *, /")
op = input("Операция: ")


if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b != 0:
        result = a / b
    else:
        result = "Ошибка: деление на 0"
else:
    result = "Неверная операция"


print(f"Результат: {result}")
