import random
import string

# Запрос длины пароля у пользователя
длина = int(input("Введите длину пароля: "))

# Все возможные символы для пароля
символы = string.ascii_letters + string.digits + string.punctuation

# Генерация случайного пароля
пароль = ''.join(random.choices(символы, k=длина))

# Вывод результата
print("Ваш случайный пароль:", пароль)
