#import os
#print("Поточна директорія запуску:", os.getcwd())
from pathlib import Path

def total_salary(path_salary):

    file_path = Path(path_salary) # перевірка наявності файлу
    if not file_path.exists():
        print(f"Файлу '{path_salary}' не існує.")
        return 0, 0

    total=0
    mid_salary=0
    n_line=0
    name=''
    salary_str=''

    with open(path_salary, 'r', encoding='utf-8') as fh:
        while True:
            try: #перевірка чи дані введено корректно (більше чим 2 значення або змінено їх порядок)
                line = fh.readline()
                if not line:
                    break
                name, salary_str = line.split(',')
                total = total+int(salary_str) #визначення загальної суми
                #print(name, salary_str)
                n_line += 1
            except ValueError:
                print(f"Увага !!!! Помилка обробки файлу. В файлі наявний рядок з помилковими даними - {line}")
        if total > 0:
            mid_salary=total/n_line #середнє значення
        else:
            None
        return (total, mid_salary)
    fh.close()

total, average = total_salary("salary.txt")

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {round(average, 2)}")

