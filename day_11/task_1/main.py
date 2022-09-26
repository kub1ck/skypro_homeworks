from data import get_data
import query


def get_transformed_data(data_list: list, command: str, value: str) -> list:
    """
    Получаем измененный список, исходя из полученной команды
    """

    # Проверка на команду и ее значения
    if command == 'filter':
        return query.filter_(data_list, value)
    elif command == 'map' and value.isdigit():
        return query.map_(data_list, value)
    elif command == 'unique' and value == '-':
        return query.unique(data_list)
    elif command == 'limit' and value.isdigit():
        return query.limit(data_list, value)
    elif command == 'sort' and value in ['asc', 'desc']:
        return query.sort_(data_list, value)
    else:
        return []


def main() -> None:
    # 'data/apache_logs.txt' - путь к файлу
    while True:
        file_path = input("Введите путь до файла с логами: ")

        if file_path == 'stop':
            break

        # Проверка на корректный путь до файла с логами
        try:
            data_list = get_data(file_path)

        except PermissionError:
            print("Укажите полный путь до файла!\n")
            continue

        except FileNotFoundError:
            print("Некорректный путь!\n")
            continue

        user_input = input("Введите команду: ")
        operations = user_input.split(' | ')

        for operation in operations:
            operation_list = operation.split()

            # Если пользователь введет только команду без значения, то выходим из программы
            if len(operation_list) != 2:
                print('Некорректная команда\n')
                exit()

            data_list = get_transformed_data(data_list, operation_list[0], operation_list[1])

            # Если команда была некорректной, то выходим
            if not data_list:
                print('Некорректная команда\n')
                exit()

        # Выводим измененный список
        for line in data_list:
            print(line)


if __name__ == "__main__":
    main()
