import argparse
from contact_manager import ContactManager

def main():
    contact_manager = ContactManager()

    # Объявление главного парсера
    parser = argparse.ArgumentParser(description="Простое CLI-приложение для управления контактами")
    # Объявление субпарсера с командами
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")
    # Передача парсера команд
    contact_manager.add_command_parsers(subparsers)
    # Парсинг аргументов
    args = parser.parse_args()
    # Выполнение команд
    contact_manager.execute_command(args)

if __name__ == "__main__":
    main()