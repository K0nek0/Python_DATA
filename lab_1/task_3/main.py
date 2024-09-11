from pathlib import Path


def create_missing_files(file_with_missing_files, target_dir):
    target_folder = Path(target_dir)

    # Проверяем, существует ли папка, и создаем её, если не существует
    if not target_folder.exists():
        target_folder.mkdir(parents=True, exist_ok=True)

    # Чтение файла с именами отсутствующих файлов
    try:
        with open(file_with_missing_files, 'r') as mf:
            missing_files = mf.read().splitlines()
    except FileNotFoundError:
        print(f"Файл {file_with_missing_files} не найден.")
        return

    # Создание отсутствующих файлов
    for file_name in missing_files:
        file_path = target_folder / file_name
        try:
            if file_path.exists():
                print(f"Файл {file_path} уже существует.")
            else:
                file_path.touch()
                print(f"Создан файл: {file_path}")
        except Exception as e:
            print(f"Ошибка при создании файла {file_name}: {e}")


if __name__ == "__main__":
    missing_files_file = input("Введите путь к файлу со списком отсутствующих файлов: ").strip()
    target_directory = input("Введите путь к папке, в которой нужно создать файлы: ").strip()

    create_missing_files(missing_files_file, target_directory)
