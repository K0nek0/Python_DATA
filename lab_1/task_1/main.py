from pathlib import Path
import shutil


def find_and_copy_small_files(folder_path='.'):
    # Преобразуем строковый путь в объект Path
    path = Path(folder_path)

    # Проверяем, существует ли заданная директория
    if not path.is_dir():
        print(f"Путь {path} не является директорией или не существует.")
        return

    # Используем glob для поиска всех txt файлов
    small_files = [file for file in path.glob('*.txt') if file.is_file() and file.stat().st_size < 2048]

    if small_files:
        print("Найдены файлы меньше 2 Кб:")
        for file in small_files:
            print(file.name)

        # Создаем папку small, если её ещё нет
        small_folder = path / 'small'
        small_folder.mkdir(parents=True, exist_ok=True)

        # Копируем все найденные файлы в папку small
        for file in small_files:
            shutil.copy(file, small_folder / file.name)
        print(f"Все файлы скопированы в папку {small_folder}")
    else:
        print("Файлы меньше 2 Кб не найдены")


if __name__ == "__main__":
    # Ввод пути к папке (или текущая папка по умолчанию)
    folder = input("Введите путь к папке (оставьте пустым для текущей): ").strip()
    if not folder:
        folder = '.'

    find_and_copy_small_files(folder)
