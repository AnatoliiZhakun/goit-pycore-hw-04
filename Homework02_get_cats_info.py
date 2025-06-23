#import os
#print("Поточна директорія запуску:", os.getcwd())
from pathlib import Path

def get_cats_info(info_cats):

    file_path = Path(info_cats) # перевірка наявності файлу
    if not file_path.exists():
        print(f"Файлу '{info_cats}' не існує.")
        return []
    
    cats_list=[]
    
    with open(info_cats, 'r', encoding='utf-8') as fh:
        while True:
            try: #перевірка чи дані введено корректно
                line = fh.readline()
                if not line:
                    break
                id, name, age = [item.strip() for item in line.split(',')]
                #print(id, name, age)
                age = int(age)  # перетворення на число
                cats_list.append({"id": id, "name": name, "age": age})
            except ValueError:
                print(f"Увага !!!! Помилка обробки файлу. В файлі наявний рядок з помилковими даними - {line}")
        return cats_list
    fh.close()

cats_info = get_cats_info("cats_file.txt")
print(cats_info)

