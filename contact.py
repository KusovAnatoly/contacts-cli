from terminaltables import AsciiTable
import json
import math
from os import path 


__file_name = "contacts.json"
'''
Название файла в котором хранится 
'''

class Contact:
    '''
    Модель, представляющая Контакт
    '''

    def __init__(self, id=0, first_name="", personal_phone="", middle_name="", last_name="", org="", work_phone=""):
        ''' Конструктор
        
        Args:
            id (int): уникальный идентификатор записи
            first_name (str): Имя
            middle_name (str): Отчество
            last_name (str): Фамилия
            org (str): Организация
            personal_phone (str): Личный телефон
            work_phone (str): Рабочий телефон
        '''

        # Проверка для уточнения произойдет работа
        # с существующим объектов либо с новым
        if id == 0:            
            self.first_name = first_name
            self.middle_name = middle_name
            self.last_name = last_name
            self.org = org
            self.personal_phone = personal_phone
            self.work_phone = work_phone
        else:
            record = get(id)
            self.id = id
            self.first_name = record['first_name']
            self.middle_name = record['middle_name']
            self.last_name = record['last_name']
            self.org = record['org']
            self.personal_phone = record['personal_phone']
            self.work_phone = record['work_phone']

    def add(self):
        '''Добавляет новый контакт в файл'''

        self.id = 1

        # Проверка на существование файла
        if path.isfile('contacts.json'):
            # Инкремент уникального идентификатора
            with open(__file_name, "r") as f:
                row_count = sum(1 for line in f)
                self.id = row_count + 1
        
        # Объект с новой записью
        new_record = {
            "id":f"{self.id}",
            "first_name":f"{self.first_name}",
            "middle_name":f"{self.middle_name}",
            "last_name":f"{self.last_name}",
            "org":f"{self.org}",
            "personal_phone":f"{self.personal_phone}",
            "work_phone":f"{self.work_phone}"
            }
        
        # Запись нового файла
        with open(__file_name, "a") as f:
            json.dump(new_record, f)
            f.write('\n')

    def edit(self):
        '''Редактирует существующий контакт в файле'''

        
        # Проверяет существует ли файл
        if not(path.isfile('contacts.json')):
            print('Контактов нет. Добавьте свой первый контакт!')
            return

        # Считывание файла и загрузка JSON-строк в качестве список словарей
        with open(__file_name, "r") as f:
            contacts = [json.loads(line) for line in f]
        
        # Поиск индекса контакта с таким же ID как и у объекта
        index = -1
        for i, contact in enumerate(contacts):
            if contact["id"] == self.id:
                index = i
                break
        
        # Если контакт найден, обновить данные в файле,
        # используя данные аттрибутов объекта
        if index != -1:
            contacts[index] = vars(self)
        
        # Запись обновленных данных в файл
        with open(__file_name, "w") as f:
            for contact in contacts:
                json.dump(contact, f)
                f.write('\n')

def get(id:int):
    '''
    Считывает из файла конкретную запись по ID

    Args:
        id (int): Идентификатор записи в файле
    '''

    if not(path.isfile('contacts.json')):        
        print('Контактов нет. Добавьте свой первый контакт!')
        return

    with open(__file_name, "r") as f:
        for line in f:
            json_obj = json.loads(line)
            if json_obj['id'] == id: # check if the id matches
                return json_obj

def read_all():
    '''
    Считывает все записи из файла
    '''
    data = []
    
    # Проверяет существует ли файл
    if not(path.isfile('contacts.json')):
        print('Контактов нет. Добавьте свой первый контакт!')
        return

    with open(__file_name, "r") as f:
        for line in f:
            json_obj = json.loads(line)
            data.append(json_obj.values())

    
    table_data = [['ID', 'First Name', 'Middle Name', 'Last Name', 'Organisation', 'Personal Phone', 'Work Phone']]
    table_data.extend(data)
    table = AsciiTable(table_data, "Контакты")
    print(table.table)

def read(page_number):
    '''
    Считывает все записи из файла по странично

    Args:
        page_number (int): Номер страницы
    '''

    if not(path.isfile('contacts.json')):        
        print('Контактов нет. Добавьте свой первый контакт!')
        return

    page_size = 10

    data = []

    with open(__file_name, "r") as f:# Skip the first line
        for line in f:
            json_obj = json.loads(line)
            data.append(json_obj.values())    

    # Расчет количества всех страниц
    total_pages = (len(data) + page_size - 1) // page_size
    
    page_data = [['ID', 'First Name', 'Middle Name', 'Last Name', 'Organisation', 'Personal Phone', 'Work Phone']]

    # Проверка пользовательского ввода страницы
    page_number = int(page_number)
    if 1 <= page_number <= total_pages:
        # Расчет стартового и конечного индексов страницы
        start_index = (page_number - 1) * page_size
        end_index = page_number * page_size
        # Получение данных через слайсинг
        page_data.extend(data[start_index:end_index])

        table = AsciiTable(page_data, f"Контакты ({page_number} из {total_pages} стр.)")
        print(table.table)
    else:
        print(f"Введите значение от {1} до {total_pages}")



def search(first_name, id=0, middle_name="", last_name="", personal_phone="", work_phone="", org=""):
    '''
    Считывает все записи из файла по странично

    Args:
        id (int): уникальный идентификатор записи
        first_name (str): Имя
        middle_name (str): Отчество
        last_name (str): Фамилия
        org (str): Организация
        personal_phone (str): Личный телефон
        work_phone (str): Рабочий телефон
    '''
    
    data = []
    
    if not(path.isfile('contacts.json')):        
        print('Контактов нет. Добавьте свой первый контакт!')
        return

    with open(__file_name, "r") as f:
        for line in f:
            json_obj = json.loads(line)
            data.append(json_obj.values())

    table_data = [['ID', 'First Name', 'Middle Name', 'Last Name', 'Organisation', 'Personal Phone', 'Work Phone']]

    # Loop over the list of lists and check if the value is in each sublist
    for i, sublist in enumerate(data):
        if first_name in sublist or middle_name in sublist or last_name in sublist or personal_phone in sublist or work_phone in sublist or org in sublist or id in sublist:
            table_data.append(sublist)
    
    table = AsciiTable(table_data, "Контакты")
    print(table.table)