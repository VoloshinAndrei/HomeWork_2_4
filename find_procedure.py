# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os
import chardet

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
migrations_dir = os.path.join(current_dir, migrations)


def get_all_filename(dirname):
    files = []
    for file in os.listdir(dirname):
        if file.endswith(".sql"):
            files.append(file)
    return files


def find_str_to_file(find_str, file_name):
    with open(os.path.join(migrations_dir, file_name), 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        s = data.decode(result['encoding']).upper()
        if find_str in s:
            result = True
            print(file_name)
        else:
            result = False
    return result


def main_def():
    filename_list = get_all_filename(migrations_dir)
    while True:
        findstr = input('Введите строку для поиска:').upper()
        filename_list_new = []
        for filename in filename_list:
            if find_str_to_file(findstr, filename):
                filename_list_new.append(filename)
        print('Всего:', len(filename_list_new))
        filename_list = filename_list_new


if __name__ == '__main__':
    # ваша логика
    main_def()
    pass
