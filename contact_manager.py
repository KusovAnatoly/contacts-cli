import sys
from contact import Contact

class ContactManager:
    
    def add_command_parsers(self, subparsers):
        '''
        Добавляет парсеры команд
        Args:
            subparsers: субпарсеры с командами
        '''
        add_command = subparsers.add_parser("add", help="Добавить новый контакт")
        add_command.add_argument("-n", "--first_name", required=True, help="Имя")
        add_command.add_argument("-m", "--middle_name", required=False, help="Отчество")
        add_command.add_argument("-l", "--last_name", required=False, help="Фамилия")
        add_command.add_argument("-o", "--org", required=False, help="Организация")
        add_command.add_argument("-pp", "--personal_phone", required=True, help="Личный телефон")
        add_command.add_argument("-wp", "--work_phone", required=False, help="Рабочий телефон")

        edit_command = subparsers.add_parser("edit", help="Редактировать контакт")
        edit_command.add_argument("-i", "--id", required=True, help="ID контакта")
        edit_command.add_argument("-n", "--first_name", required=False, help="Имя")
        edit_command.add_argument("-m", "--middle_name", required=False, help="Отчество")
        edit_command.add_argument("-l", "--last_name", required=False, help="Фамилия")
        edit_command.add_argument("-o", "--org", required=False, help="Организация")
        edit_command.add_argument("-pp", "--personal_phone", required=True, help="Личный телефон")
        edit_command.add_argument("-wp", "--work_phone", required=False, help="Рабочий телефон")

        list_command = subparsers.add_parser("list", help="Отобразить контакты")
        list_command.add_argument("-a", "--all", action="store_true", help="Отобразить все")
        list_command.add_argument("-pn", "--page_number", type=int, help="Отобразить постранично")

        search_command = subparsers.add_parser("search", help="Найти контакты")
        search_command.add_argument("-i", "--id", required=True, help="ID контакта")
        search_command.add_argument("-n", "--first_name", required=False, help="Имя")
        search_command.add_argument("-m", "--middle_name", required=False, help="Отчество")
        search_command.add_argument("-l", "--last_name", required=False, help="Фамилия")
        search_command.add_argument("-o", "--org", required=False, help="Организация")
        search_command.add_argument("-pp", "--personal_phone", required=True, help="Личный телефон")
        search_command.add_argument("-wp", "--work_phone", required=False, help="Рабочий телефон")

    def add_contact(self, args):
        contact = Contact(first_name=args.first_name, middle_name=args.middle_name,
                          last_name=args.last_name, org=args.org,
                          personal_phone=args.personal_phone, work_phone=args.work_phone)
        contact.add()
        print(f"Новый контакт \"{contact.first_name}\" был создан")

    def edit_contact(self, args):
        contact = Contact(args.id)
        contact.update(args)
        print(f"Конакт \"{contact.first_name}\" был отредактирован")

    def list_contacts(self, args):
        contacts = Contact.read_all()
        if contacts:
            for contact in contacts:
                print(contact)
        else:
            print("Контактов не найдено")

    def search_contacts(self, args):
        search_params = vars(args)
        del search_params['command']
        results = Contact.search(**search_params)
        if results:
            for contact in results:
                print(contact)
        else:
            print("Такой контакт не найден")
    
    def execute_command(self, args):
        '''
        Выполняет команды
        Args:
            args: выполняемая команда
        '''
        if args.command == "add":
            self.add_contact(args)
        elif args.command == "edit":
            self.edit_contact(args)
        elif args.command == "list":
            self.list_contacts(args)
        elif args.command == "search":
            self.search_contacts(args)
        else:
            print("Неизвестная команда")
            sys.exit(1)