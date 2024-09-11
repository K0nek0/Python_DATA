import sys
from pathlib import Path


def check_files_in_directory(path, file_names):
    path = Path(path)

    if not path.is_dir():
        return

    if file_names:
        existing_files = []
        missing_files = []

        for file_name in file_names:
            file_path = path / file_name
            if file_path.exists():
                existing_files.append(file_name)
            else:
                missing_files.append(file_name)

        print("Существующие файлы:")
        print("\n".join(existing_files) if existing_files else "Нет существующих файлов")

        print("\nОтсутствующие файлы:")
        print("\n".join(missing_files) if missing_files else "Нет отсутствующих файлов")

        with open('existing_files.txt', 'w') as ef:
            ef.write("\n".join(existing_files))

        with open('missing_files.txt', 'w') as mf:
            mf.write("\n".join(missing_files))

        print("\nРезультаты записаны в файлы 'existing_files.txt' и 'missing_files.txt'")
    else:
        # Если имена файлов не указаны, выводим общую информацию о папке
        files = [f for f in path.iterdir() if f.is_file()]
        total_size = sum(f.stat().st_size for f in files)

        print(f"Количество файлов: {len(files)}")
        print(f"Общий размер файлов: {total_size} байт")


if __name__ == "__main__":
    args = sys.argv[1:]  # Получаем аргументы командной строки
    path = '.'

    # Поиск аргумента --path
    if '--path' in args:
        path_index = args.index('--path')
        if path_index + 1 < len(args):
            path = args[path_index + 1]
        else:
            print("Ошибка: не указан путь после --path")
            sys.exit(1)

    # Поиск аргумента --files
    if '--files' in args:
        files_index = args.index('--files')
        file_names = args[files_index + 1:]
    else:
        file_names = []

    check_files_in_directory(path, file_names)
