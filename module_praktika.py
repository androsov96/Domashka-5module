class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            if len(password) >= 8 and any(i.isupper() for i in password):
                self.password = password
            else:
                print("Пароль должен содержать минимум 8 символов и хотя-бы одну заглавную букву")

if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input("Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n"))
        if choice == 1:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f"Добро пожаловать,{login}")
                    break
                else:
                    print("Пароль неверный.")
            else:
                print("Пользователь с таким именем не найден. ")
        if choice == 2:
            user = User(input('Введите логин: '), password := input("Введите пароль: "),
                        password2 := input("Повторите пароль: "))
            if password != password2:
                print("Пароли не совпадают. ")
                continue
            database.add_user(user.username, user.password)
        print(database.data)