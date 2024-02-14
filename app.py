import argparse
import json
import sys
from contact import read_all
from contact import read
from contact import search
from contact import Contact

# Создание объекта-парсера
parser = argparse.ArgumentParser(description="Простое CLI-приложение для управления контактами")

# Создание объекта субпарсера
add_parser = parser.add_subparsers(dest="command")

# Установление атрибута "Требуется" для субпарсера
add_parser.required = True

# Объявление команды Добавить
add_command = add_parser.add_parser("add", help="Добавить новый контакт")
add_command.add_argument("-n", "--first_name", required=True, help="Имя контакта")
add_command.add_argument("-l", "--last_name", required=False, help="Фамилия контакта")
add_command.add_argument("-m", "--middle_name", required=False, help="Отчество контакта")
add_command.add_argument("-o", "--org", required=False, help="Электронный адрес контакта")
add_command.add_argument("-pp", "--personal_phone", required=True, help="Личный телефон")
add_command.add_argument("-wp", "--work_phone", required=False, help="Рабочий телефон")

# Объявление команды Редактировать
edit_command = add_parser.add_parser("edit", help="Редактировать контакт")
edit_command.add_argument("-i", "--id", required=True, help="Идентификатор контакта")
edit_command.add_argument("-n", "--first_name", required=False, help="Имя контакта")
edit_command.add_argument("-l", "--last_name", required=False, help="Фамилия контакта")
edit_command.add_argument("-m", "--middle_name", required=False, help="Отчество контакта")
edit_command.add_argument("-o", "--org", required=False, help="Электронный адрес контакта")
edit_command.add_argument("-pp", "--personal_phone", required=False, help="Личный телефон")
edit_command.add_argument("-wp", "--work_phone", required=False, help="Рабочий телефон")

# Объявление команды Показать
show_command = add_parser.add_parser("show", help="Показать контакты")
show_command.add_argument("-a", "--all", required=False, action="store_true", help="Все записи")
show_command.add_argument("-pn", "--page_number", required=False, help="Номер страницы")

# Объявление команды Найти
search_command = add_parser.add_parser("search", help="Найти контакты")
search_command.add_argument("-i", "--id", required=False, help="Идентификатор контакта")
search_command.add_argument("-n", "--first_name", required=False, help="Имя контакта")
search_command.add_argument("-l", "--last_name", required=False, help="Фамилия контакта")
search_command.add_argument("-m", "--middle_name", required=False, help="Отчество контакта")
search_command.add_argument("-o", "--org", required=False, help="Электронный адрес контакта")
search_command.add_argument("-pp", "--personal_phone", required=False, help="Личный телефон")
search_command.add_argument("-wp", "--work_phone", required=False, help="Рабочий телефон")

args = parser.parse_args()

# Объявление команды Добавить
if args.command == "add":
    if not args.first_name:
        print('Ошибка. Параметр -n | --first_name (\'Имя\') обязателен для использования')
        sys.exit(0)
    
    if not args.first_name:
        print('Ошибка. Параметр -pp | --personal_phone (\'Личный телефон\') обязателен для использования')
        sys.exit(0)
    
    contact = Contact(first_name=args.first_name, middle_name=args.middle_name, last_name=args.last_name, org=args.org, personal_phone=args.personal_phone, work_phone=args.work_phone)
    contact.add()
    print(f"Новый контакт \"{contact.first_name}\" был добавлен")

# Проверка команды из аргументов на соотвествие
if args.command == "edit":

    if not str(args.id).isdigit():
        print('Ошибка. Параметр -i | --id (\'Идентификатор контакта\') обязателен для использования и должен быть целым. Узнать ID можно посмотрев список контактов')
        sys.exit(0)

    contact = Contact(int(args.id))

    if args.first_name:
        contact.first_name = args.first_name
    if args.middle_name:
        contact.middle_name = args.middle_name
    if args.last_name:
        contact.last_name = args.last_name
    if args.personal_phone:
        contact.personal_phone = args.personal_phone
    if args.work_phone:
        contact.work_phone = args.work_phone
    if args.org:
        contact.org = args.org

    contact.edit()

    print(f"Контакт \"{contact.first_name}\" был отредактирован")

if args.command == "show":
    if not args.all and not args.page_number:
        print('Ошибка: вы не указали параметр -p | --page_number (Номер страницы) либо -a | --all (Все записи)')
        sys.exit(0)

    if args.all:
        read_all()

    if args.page_number:
        if str(args.page_number).isdigit():
            read(int(args.page_number))
        else:
            print('Ошибка: параметр -p | --page_number (Номер страницы) должен быть целым целым числом')
            sys.exit(0)

if args.command == "search":
    if args.id or args.first_name or args.middle_name or args.last_name or args.personal_phone or args.work_phone or args.org:
        id = 0
        if str(args.id).isdigit():
            id = int(args.id)
        
        search(id=id, first_name=args.first_name, middle_name=args.middle_name, last_name=args.last_name, personal_phone=args.personal_phone, work_phone=args.work_phone, org=args.org)
    else:
        print('Ошибка: вы не использовали ни один параметр для поиска. Если вам не нужен поиск, воспользуйтесь командой show')
        sys.exit(0)