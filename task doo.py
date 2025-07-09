def display_menu():
    print("\nСписок дел - Меню:")
    print("1. Показать все задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Выйти")

def show_tasks(tasks):
    if not tasks:
        print("\nВаш список задач пуст.")
    else:
        print("\nВаши задачи:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Введите новую задачу: ")
    tasks.append(task)
    print(f"Задача '{task}' добавлена.")

def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Введите номер задачи для удаления: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Задача '{removed_task}' удалена.")
            else:
                print("Неверный номер задачи.")
        except ValueError:
            print("Пожалуйста, введите корректный номер.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nВыберите действие (1-4): ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Выход из приложения. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
