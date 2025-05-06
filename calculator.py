def add(x, y): 

    """Складывает два числа.""" 

    return x + y 

 

def subtract(x, y): 

    """Вычитает одно число из другого.""" 

    return x - y 

 

def multiply(x, y): 

    """Умножает два числа.""" 

    return x * y 

 

def divide(x, y): 

    """Делит одно число на другое. Обрабатывает деление на ноль.""" 

    if y == 0: 

        return "Ошибка! Деление на ноль." 

    return x / y 

 

while True: 

    print("\nВыберите операцию:") 

    print("1. Сложение") 

    print("2. Вычитание") 

    print("3. Умножение") 

    print("4. Деление") 

    print("5. Выход") 

 

    choice = input("Введите номер операции (1-5): ") 

 

    if choice in ('1', '2', '3', '4'): 

        try: 

            num1 = float(input("Введите первое число: ")) 

            num2 = float(input("Введите второе число: ")) 

        except ValueError: 

            print("Ошибка! Введите числовые значения.") 

            continue 

 

        if choice == '1': 

            print(num1, "+", num2, "=", add(num1, num2)) 

        elif choice == '2': 

            print(num1, "-", num2, "=", subtract(num1, num2)) 

        elif choice == '3': 

            print(num1, "*", num2, "=", multiply(num1, num2)) 

        elif choice == '4': 

            print(num1, "/", num2, "=", divide(num1, num2)) 

    elif choice == '5': 

        print("Выход из калькулятора.") 

        break 

    else: 

        print("Некорректный ввод. Пожалуйста, выберите операцию из списка.") 