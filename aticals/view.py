def add_title(title):
    def wraper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" *50)
            return output
        return wrap
    return wraper
    # pass


class UserInterfase:
    @add_title("Ввод пользовательских данных")
    def wait_user_answer(self):
        # print(" Ввод пользовательских данных ".center(50, "="))
        print("Действие со статьями: ")
        print("1 - создание статьи"
              "\n2 - просмотр статей"
              "\n3 - просмотр отдельной статьи"
              "\n4 - удаление статьи"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        # print("=" *50)
        return user_answer

    @add_title("Создание статьи: ")
    def add_user_aticals(self):
        dict_atical={
            "Название": None,
            "Автор": None,
            "Количество страниц": None,
            "Описание": None
        }
        # print(" Создание статьи: ".center(50, "="))
        for key in dict_atical:
            dict_atical[key] = input(f"Введите {key} статьи: ")
        # print("=" * 50)
        return dict_atical

    @add_title("Список статей:")
    def show_all_aticals(self, aticals):
        # print("Список статей: ".center(50, '='))
        for ind, atical in enumerate(aticals, 1):
            print(f'{ind}. {atical}')
        # print("=" * 50)

    @add_title("Ввод названия статьи:")
    def get_user_atical(self):
        user_atical = input("Введите название статьи: ")
        return user_atical

    @add_title("Промотр статьи:")
    def show_single_atical(self, atical):
        for key in atical:
            print(f"{key} статьи - {atical[key]}")

    @add_title("Сообщение об ошибке")
    def show_incorrect_title_error(self, user_title):
        print(f'Статьи с названием {user_title} не существует')

    @add_title("Удаление статьи:")
    def remove_single_atical(self, atical):
        print(f"Статья {atical} была удалена")

    @add_title("Сообщение об ошибке")
    def show_incorrect_answer_error(self, user_answer):
        print(f'Варианта {user_answer} не существует')
