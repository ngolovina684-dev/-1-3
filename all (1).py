# Менеджер личных расходов

expenses = []

def add_expense():
    name = input("Введите название покупки: ")
    cost = float(input("Введите стоимость: "))

    expense = {
        "name": name,
        "cost": cost
    }

    expenses.append(expense)
    print("Расход добавлен!")

def show_expenses():
    if len(expenses) == 0:
        print("Список расходов пуст.")
        return

    total = 0

    print("\nВаши расходы:")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - {expense['cost']} руб.")
        total += expense['cost']

    print(f"\nОбщая сумма: {total} руб.")

def find_expense():
    search = input("Введите название покупки: ")

    found = False

    for expense in expenses:
        if expense["name"].lower() == search.lower():
            print(f"Найдено: {expense['name']} - {expense['cost']} руб.")
            found = True

    if not found:
        print("Такой покупки нет.")

def delete_expense():
    delete_name = input("Введите название покупки для удаления: ")

    for expense in expenses:
        if expense["name"].lower() == delete_name.lower():
            expenses.remove(expense)
            print("Запись удалена.")
            return

    print("Покупка не найдена.")

def save_to_file():
    file = open("expenses.txt", "w", encoding="utf-8")

    for expense in expenses:
        file.write(f"{expense['name']};{expense['cost']}\n")

    file.close()

    print("Данные сохранены.")

def load_from_file():
    try:
        file = open("expenses.txt", "r", encoding="utf-8")

        expenses.clear()

        for line in file:
            name, cost = line.strip().split(";")

            expenses.append({
                "name": name,
                "cost": float(cost)
            })

        file.close()

        print("Данные загружены.")

    except FileNotFoundError:
        print("Файл пока не существует.")

while True:

    print("\n===== МЕНЕДЖЕР РАСХОДОВ =====")
    print("1. Добавить расход")
    print("2. Показать расходы")
    print("3. Найти расход")
    print("4. Удалить расход")
    print("5. Сохранить в файл")
    print("6. Загрузить из файла")
    print("7. Выход")

    choice = input("Выберите пункт: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        find_expense()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        save_to_file()

    elif choice == "6":
        load_from_file()

    elif choice == "7":
        print("Программа завершена.")
        break

    else:
        print("Неверный выбор.")