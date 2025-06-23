def parse_input(user_input): # модуль розподілу команда + додаткові параметри
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts): # модуль добавки контакту
    try:
        name, phone = args # перевірка корректності параметрів - наявне як ім'я так і номер
    except ValueError:
        return "Error: Please provide both name and phone."
    if name in contacts:
        return "Error: Contact already exists." # якщо ім'я вже є новий номер не перезатирає поверх
    else:
        contacts[name] = phone # добавка номеру
        return "Contact added."

def change_contact(args, contacts): # зміна номеру
    try:
        name, phone = args  # перевірка корректності параметрів - наявне як ім'я так і номер
    except ValueError:
        return "Error: Please provide both name and phone."
    if name in contacts: # ім'я наявне в списку
        contacts[name] = phone
        return "Contact phone change."
    else:                # ім'я відсутнє в списку
        return("Error: Contact not found")  
    
def show_phone(args, contacts):
    name = args [0]
    if name in contacts: # ім'я наявне в списку
        return ("Contact phone :" + contacts[name])
    else:                # ім'я відсутнє в списку
        return("Error: Contact not found")   
    
def all_phone(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])  # вивід списку построково

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]: # команда вихід
            print("Good bye!")
            break
        elif command in ["hello", "hi"]: # команда привіт
            print("How can I help you?")
        elif command == "add":            # команда добавити номер
            print(add_contact(args, contacts))
        elif command == "change":         # команда змінити номер
            print(change_contact(args, contacts))
        elif command == "phone":          # команда на запит номеру
            print(show_phone(args, contacts))
        elif command == "all":            # команда вивести все
            print(all_phone (contacts))

        else:
            print("Error: Invalid command.")    # команда не визначена

if __name__ == "__main__":
    main()