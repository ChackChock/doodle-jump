import pygame

from scripts.app import App


def main():
    pygame.init()  # Запуск библиотеки pygame

    app = App()  # Создание приложения
    app.run()    # Запуск игрового цикла


# Точка входа
if __name__ == "__main__":
    main()
