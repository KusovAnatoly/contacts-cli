# Contact CLI

Contact CLI - просто CLI-приложение, которое позволяет добавлять, редактировать, отобрадать и искать контакты. Оно использует JSON-файл для хреняния информации о контактах.

## Функции

- Добавлять новый контакт
- Редактировать существующие контакты по их ID
- Отображать все контакты, а также постраничное отображение
- Искать контакты по любым полям

## Использование

Чтобы воспользоваться Contact CLI вам необходимо иметь Python 3 и pip на своем компьютере. Дале следуйте следующим шагам:

- Склонируйте репозиторий: `git clone https://github.com/your-username/contact-manager.git`
- Перейдите к директории с проектом: `cd contact-cli`
- Установите необходимые пакеты: `pip install -r requirements.txt`
- Запустите приложения используя различные команды: `python app.py --help`

Приложение имеет четыре команды: `add`, `edit`, `show`, and `search`. Каждая команда имеет свои аргументы, вы можете узнать подробнее используя команды  `-h` or `--help`

## Примечание

В репозитории имеется тестовый файл contacts.json. Если вы хотите добавить свои контакты, удалите файл и воспользуйтесь командой `add`

## Примеры команд

```
python app.py add -n Ivan -p '+7(905)772-78-50'
```

```
python app.py edit -i 1001 -n Igor
```

```
python app.py search -n Ulberto
```

```
python app.py show --p 10
```

```
python app.py show -a
```