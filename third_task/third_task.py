import sys
from pathlib import Path
from colorama import init, Fore, Style

init()  

def print_tree(path, indent=0):
    try:
        for item in path.iterdir():
            if item.is_dir():
                print(" " * indent + Fore.BLUE + item.name + "/" + Style.RESET_ALL)
                print_tree(item, indent + 2)
            else:
                print(" " * indent + Fore.GREEN + item.name + Style.RESET_ALL)
    except PermissionError:
        print(" " * indent + Fore.RED + "[Доступ заборонено]" + Style.RESET_ALL)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Використовуйте скрипт правильно: python third_task.py <шлях_до_директорії>")
    else:
        root = Path(sys.argv[1])
        if root.exists() and root.is_dir():
            print(Fore.BLUE + root.name + "/" + Style.RESET_ALL)
            print_tree(root, 2)
        else:
            print(Fore.RED + "Помилка: вкажіть існуючу директорію")

