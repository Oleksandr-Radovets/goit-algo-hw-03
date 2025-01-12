import os
import shutil
import argparse

def process_directory(source, destination):
    try:
        for item in os.listdir(source):
            item_path = os.path.join(source, item)

            if os.path.isdir(item_path):
                process_directory(item_path, destination)
            elif os.path.isfile(item_path):
                ext = os.path.splitext(item)[1][1:] or "no_extension"
                ext_dir = os.path.join(destination, ext)

                os.makedirs(ext_dir, exist_ok=True)

                shutil.copy2(item_path, ext_dir)
    except Exception as e:
        print(f"Помилка при обробці '{source}': {e}")


def main():
    parser = argparse.ArgumentParser(description="Копіює файли з сортуванням за розширеннями.")
    parser.add_argument("source", help="Шлях до вихідної директорії.")
    parser.add_argument("destination", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням 'dist').")
    args = parser.parse_args()

    if not os.path.exists(args.source) or not os.path.isdir(args.source):
        print(f"Вихідна директорія '{args.source}' не існує або не є директорією!")
        return

    os.makedirs(args.destination, exist_ok=True)

    process_directory(args.source, args.destination)
    print(f"Файли успішно скопійовано до '{args.destination}'.")


if __name__ == "__main__":
    main()