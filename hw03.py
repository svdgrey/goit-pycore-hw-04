import sys
from pathlib import Path
from colorama import Fore, Style


# Recursive function that prints the directory structure with colored view for directories and files
# Blue color is used for directories
# Green color is used for files
# parameters:
# - path: the directory path to display
# - level: the current indentation level (default is 0)
# - max_level: the maximum depth to display (0 - no limit)  
def show_directory(path: Path, level=0, max_level=0):
    for item in sorted(path.iterdir()):
        indent = "   " * level

        if item.is_dir():
            print(Fore.BLUE + indent + item.name + "/" + Style.RESET_ALL)
            if max_level == 0 or level < max_level:
                show_directory(item, level + 1, max_level)
        else:
            print(Fore.GREEN + indent + item.name + Style.RESET_ALL)


def main():

    if len(sys.argv) < 2:
        print(Fore.RED + "Помилка: вкажіть шлях до директорії.")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print(Fore.RED + "Помилка: вказаний шлях не існує.")
        return

    if not path.is_dir():
        print(Fore.RED + "Помилка: вказаний шлях не є директорією.")
        return

    print(Fore.BLUE + path.name + "/" + Style.RESET_ALL)
    show_directory(path, 1)


if __name__ == "__main__":
    main()
