import argparse
import json
import sys
from contact import read_all
from contact import read
from contact import search
from contact import Contact

def main():
    contact_manager = ContactManager()

    # Объявление главного парсера
    parser = argparse.ArgumentParser(description="Простое CLI-приложение для управления контактами")
    # Объявление субпарсера с командами
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")
    # Парсинг аргументов
    args = parser.parse_args()
    # Передача аргументов командной строки
    contact_manager.execute_command(args)
    # Выполнение команд
    contact_manager.add_command_parsers(subparsers)

if __name__ == "__main__":
    main()