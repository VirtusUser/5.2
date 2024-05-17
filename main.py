def calculate():
    while True:
        try:

            num1 = float(input("Введіть перше число: "))
            operator = input("Введіть операцію (+, -, *, /): ")
            num2 = float(input("Введіть друге число: "))


            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Помилка: ділення на нуль!")
                    continue
            else:
                print("Невідома операція!")
                continue

            print(f"Результат: {result}")

        except ValueError:
            print("Помилка: введено некоректне число!")
            continue


        again = input("Бажаєте продовжити (y/n)? ").strip().lower()
        if again != 'y':
            break