import os

# Полная структура заголовков с ключами в кавычках
titles = {
    "1": "О системе",
    "1.1": "Наименование и обозначение системы",
    "1.2": "Область применения системы",
    "1.3": "Основные функции системы",
    "1.4": "Роли пользователей",
    "2": "Работа в системе",
    "1.5": "Запуск системы",
    "1.6": "Авторизация",
    "1.7": "Просмотр информации о системе",
    "1.8": "Настройка шлюзов автоматизации",
    "1.8.1": "Добавление шлюза",
    "1.8.2": "Статусы шлюза",
    "1.8.3": "Состояния шлюза",
    "1.8.4": "Удаление шлюза",
    "1.9": "Управление учетными записями",
    "1.9.1": "Создание УЗ",
    "1.9.2": "Редактирование УЗ",
    "1.9.3": "Удаление УЗ",
    "1.10": "Иерархия моделей ПО",
    "1.10.1": "Уровни моделей ПО",
    "1.10.2": "Создание модели ПО",
    "1.10.3": "Добавление связей между моделями ПО",
    "1.10.4": "Переименование модели ПО",
    "1.10.5": "Редактирование свойств модели ПО",
    "1.10.6": "Редактирование свойств применимости модели ПО",
    "1.10.7": "Удаление связей между моделями ПО",
    "1.10.8": "Удаление модели ПО",
    "1.11": "Управление шаблонами",
    "1.11.1": "Выбор актуальной версии шаблона",
    "1.11.2": "Загрузка и обновление шаблона",
    "1.11.3": "Создание шаблона",
    "1.11.4": "Выгрузка шаблонов",
    "1.12": "Управление профилями",
    "1.12.1": "Создание профиля из списка профилей",
    "1.12.2": "Копирование профиля",
    "1.12.3": "Создание профиля через перечень шаблонов",
    "1.12.4": "Редактирование требований профиля",
    "1.12.5": "Переименование профиля",
    "1.12.6": "Смена применимости профиля",
    "1.12.7": "Активация профиля",
    "1.12.8": "Архивация профиля",
    "1.12.9": "Удаление профиля",
    "1.13": "Управление требованиями",
    "1.13.1": "Добавление раздела",
    "1.13.2": "Переименование раздела",
    "1.13.3": "Перемещение раздела",
    "1.13.4": "Удаление раздела",
    "1.13.5": "Создание требования",
    "1.13.6": "Добавление сведений",
    "1.13.7": "Добавление применимости",
    "1.13.8": "Добавление данных сбора конфигурации",
    "1.13.9": "Добавление данных анализа конфигурации",
    "1.13.10": "Добавление данных исправления конфигурации",
    "1.13.11": "Добавление требования из Единого реестра требований",
    "1.13.12": "Переименование требования",
    "1.13.13": "Редактирование данных требования",
    "1.13.14": "Смена применимости требования",
    "1.13.15": "Использование отметки «Черновик»",
    "1.13.16": "Удаление требования",
    "1.14": "Управление ресурсами",
    "1.14.1": "Добавление раздела",
    "1.14.2": "Переименование раздела",
    "1.14.3": "Перемещение раздела",
    "1.14.4": "Удаление раздела",
    "1.14.5": "Создание online-ресурса",
    "1.14.6": "Создание offline-ресурса",
    "1.14.7": "Переименование ресурса",
    "1.14.8": "Перемещение ресурса",
    "1.14.9": "Редактирование данных ресурса",
    "1.14.10": "Редактирование программной топологии",
    "1.14.11": "Добавление экземпляра ПО",
    "1.14.11.1": "Добавление экземпляра уровеня 1",
    "1.14.11.2": "Добавление экземпляра уровеня 2",
    "1.14.12": "Редактирование экземпляра ПО",
    "1.14.13": "Импорт и экспорт ресурсов",
    "1.14.13.1": "Содержимое файла экспорта",
    "1.14.13.2": "Импорт ресурса",
    "1.14.13.3": "Экспорт ресурса",
    "1.14.14": "Удаление экземпляра ПО",
    "1.14.15": "Удаление ресурса",
    "1.15": "Аудит конфигурации ПО",
    "1.15.1": "Создание области аудита",
    "1.15.2": "Редактирование области аудита",
    "1.15.3": "Задачи на аудит",
    "1.15.4": "Запуск задачи",
    "1.15.5": "Отмена задачи",
    "1.15.6": "Просмотр отчета аудита",
    "1.15.6.1": "Просмотр отчета",
    "1.15.6.2": "Группировка подзадач",
    "1.15.6.3": "Скачивание отчета",
    "1.15.7": "Просмотр протокола аудита",
    "1.15.7.1": "Просмотр протокола",
    "1.15.7.2": "Статистика проверок",
    "1.15.7.3": "Список требований",
    "1.15.7.4": "Смена отображения требований",
    "1.15.7.5": "Фильтрация требований",
    "1.15.8": "Завершение протокола аудита",
    "1.15.8.1": "Завершение сбора конфигурации",
    "1.15.8.2": "Завершение анализа конфигурации",
    "1.15.9": "Удаление области аудита",
    "3": "Дополнительная информация",
    "1.16": "Сообщения об ошибках",
}

# Путь к папке images
images_folder = "images"

# Получаем список всех файлов в папке images
all_files = os.listdir(images_folder)
print(all_files)


# Функция для проверки, начинается ли имя файла с определенного номера
def get_files_by_number(number):
    return [f for f in all_files if f.startswith(str(number)+'_')]


# Создаем словарь для хранения названий файлов по заголовкам
files_by_titles = {}

# Заполняем словарь
for number in titles:
    files_by_titles[number] = get_files_by_number(number)

# Выводим результат
for title_number, files in files_by_titles.items():
    print(f"Заголовок {title_number}: {titles[title_number]}")
    print(f"Файлы: {files}")
