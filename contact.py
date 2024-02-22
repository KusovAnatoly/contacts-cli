import json
from os import path

_file_name = "contacts.json"

class Contact:
    def __init__(self, id=0, first_name="", personal_phone="", middle_name="", last_name="", org="", work_phone=""):
        if id == 0:
            self.first_name = first_name
            self.middle_name = middle_name
            self.last_name = last_name
            self.org = org
            self.personal_phone = personal_phone
            self.work_phone = work_phone
        else:
            record = self._get(id)
            if record:
                self.__dict__.update(record)
            else:
                raise ValueError("Контакт не найдеен")

    def add(self):
        '''
        Добавляет новый контакт
        '''
        new_record = {
            "id": self._generate_id(),
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "last_name": self.last_name,
            "org": self.org,
            "personal_phone": self.personal_phone,
            "work_phone": self.work_phone
        }
        with open(_file_name, "a") as f:
            json.dump(new_record, f)
            f.write('\n')

    def update(self, args):
        '''
        Обновляет контакт
        Args:
            args: данные для обновления
        '''
        # Загрузка существующих контактов
        contacts = self._read_contacts()

        # Найти контакт для редактирования
        for contact in contacts:
            if contact['id'] == args.id:
                # Обновить поля контакта с ненулевыми значениями
                for key, value in vars(args).items():
                    if value is not None:
                        contact[key] = value
                break
        
        # Записать контакты обратно в файл
        with open(_file_name, "w") as f:
            for contact in contacts:
                json.dump(contact, f)
                f.write('\n')

    def _get(self, id):
        contacts = self._read_contacts()
        for contact in contacts:
            if contact['id'] == id:
                return contact
        return None

    @staticmethod
    def _read_contacts():
        contacts = []
        if path.isfile(_file_name):
            with open(_file_name, "r") as f:
                for line in f:
                    obj = json.loads(line)
                    contacts.append(obj.values())
                return contacts
        else:
            print('Контактов нет')

    @staticmethod
    def _generate_id():
        contacts = Contact._read_contacts()
        if contacts:
            return max(contact['id'] for contact in contacts) + 1
        else:
            return 1

    @staticmethod
    def read_all():
        '''
        Считывает все контакты
        '''
        contacts = Contact._read_contacts()
        return contacts

    @staticmethod
    def read(page_number):
        '''
        Считывает все контакты по номеру страницы
        Args:
            page_number (int): номер страницы
        '''
        contacts = Contact._read_contacts()
        page_size = 10
        start_index = (page_number - 1) * page_size
        end_index = page_number * page_size
        return contacts[start_index:end_index]

    @staticmethod
    def search(**kwargs):
        '''
        Исчет по всем аттрибутам контакта
        '''
        contacts = Contact._read_contacts()
        result = []
        for contact in contacts:
            match = True
            for key, value in kwargs.items():
                if getattr(contact, key, None) != value:
                    match = False
                    break
            if match:
                result.append(contact)
        return result