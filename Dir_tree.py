from colorama import Fore
from pathlib import Path


def dir_find_file(path_dir, level=0):
    path = Path(path_dir)
    
    # Виводимо саму директорію
    print(Fore.BLUE + f"{' '*level*3 +'└──' } {path.name}/" + Fore.RESET)

    for item in path.iterdir():
        if item.is_dir():
            # рекурсія для підпапок
            dir_find_file(item, level + 1)
        else:
            # виводимо файл з відступом
            print(Fore.GREEN + f"{' '* (level+1) *3 +'├──'} {item.name}" + Fore.RESET)


path_main = input('Введіть директорію для побудови дерева каталогів: ')
path = Path(path_main)
if not path.exists():
    print(f"Папки '{path}' не існує.")
elif not path.is_dir():
    print(f"'{path}' — це не директорія.")
else:
    dir_find_file(path_main)

