#Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
#Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
#Программа должна выводить данные
#Программа должна сохранять данные в текстовом файле
#Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
#Использование функций. Ваша программа не должна быть линейной

#1. Создать файл phonebook.txt
# - обратимся к файлу phonebook.txt в режиме append ('a')
#
# ('phonebook.txt','a')

#2. Ввод данных (запись контакта)
# - получить от пользователя данные по новомму контакту
# - подготовить данные к записи
# - обратимся к файлу phonebook.txt в режиме append ('a')
# - добавить полученные данные

#3. Вывод данных на экран
# - обратимся к файлу phonebook.txt в режиме read ('r')
# - вывести на экран все данные из файла

#4. Пользовательский поиск по характеристике
#- выбрать вариант поиска (по имени фамилий или телефону)
#- получить данные для поиска
#- обратимся к файлу phonebook.txt в режиме read ('r')
#- осуществим поиск по файлу
#- выведем на экран (если найдем совпадаение)

#5. Пользовательский интерфейс 
# Просто сделать


def file_read():
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        return file.read()

def file_append(text=""):
    with open("phonebook.txt", "a", encoding="UTF-8") as file:
        file.write(text)

# Функции ввода
def input_sur():
    return input("Введите фамилию:")

def input_name(): 
    return input("Введите Имя:")

def input_pat(): 
    return input("Введите отчество:")

def input_phone(): 
    return input("Введите телефон:")

def input_adr(): 
    return input("Введите адрес:")

# Функции ввода
def input_data():
    sur = input_sur()
    name = input_name()
    pat =input_pat()
    phone =input_phone()
    adr = input_adr()
    contact_str = f"{sur}  {name} {pat}  {phone}\n{adr}\n\n" #Форматирование для записи
    file_append(contact_str)

def print_data():
    print(file_read())    

def search_contact():
    print("Возможные варианты поиска:\n"
          "1. По фамилии\n"
          "2. По имени\n"
          "3. По отчеству\n" 
          "4. По номеру телефона\n"
          "5. По адресу\n")
    command = input("Выберите вариант поиска:")
    while command not in ("1","2","3","4","5"):
        print("Некорректный ввод, повторите попытку")
        command = input("Выберите вариант поиска:")
    i_var = int(command) - 1
    search = input("Введите данные для поиска:")
    print()
    contacts_list = file_read().rstrip().split("\n\n")
    for contact_str in contacts_list:
        cont_list = contact_str.replace("\n"," ").split()
        if search in cont_list[i_var]: 
            print(contact_str)
            print()

# Функция изменения данных контакта
def update_contact():
    search = input("Введите имя или фамилию контакта для изменения данных:")
    contacts_list = file_read().rstrip().split("\n\n")
    for index, contact_str in enumerate(contacts_list):
        cont_list = contact_str.replace("\n", " ").split()
        if search in cont_list:
            print("Найден контакт:")
            print(contact_str)
            print()
            print("Введите новые данные для контакта:")
            sur = input_sur()
            name = input_name()
            pat = input_pat()
            phone = input_phone()
            adr = input_adr()
            new_contact_str = f"{sur}  {name} {pat}  {phone}\n{adr}\n\n"
            contacts_list[index] = new_contact_str
            break
    else:
        print("Контакт не найден.")
    updated_contacts = "\n\n".join(contacts_list)
    with open("phonebook.txt", "w", encoding="UTF-8") as file:
        file.write(updated_contacts)
        print("Данные контакта успешно изменены.")

# Функция удаления контакта
def delete_contact():
    search = input("Введите имя или фамилию контакта для удаления:")
    contacts_list = file_read().rstrip().split("\n\n")
    found = False
    for index, contact_str in enumerate(contacts_list):
        cont_list = contact_str.replace("\n", " ").split()
        if search in cont_list:
            print("Найден контакт:")
            print(contact_str)
            print()
            confirmation = input("Вы уверены, что хотите удалить контакт? (y/n):")
            if confirmation.lower() == "y":
                del contacts_list[index]
                found = True
                break
            else:
                print("Удаление отменено.")
                return
    if not found:
        print("Контакт не найден.")
    else:
        updated_contacts = "\n\n".join(contacts_list)
        with open("phonebook.txt", "w", encoding="UTF-8") as file:
            file.write(updated_contacts)
            print("Контакт успешно удален.")

# User menu (interface)
def u_interface():
    file_append() #- создание файла
    command = ""
    while command != "5":
        print("Меню:\n"
            "1. Добавить контакт\n"
            "2. Найти контакт\n"
            "3. Вывести все контакты\n" 
            "4. Изменить контакт\n"
            "5. Удалить контакт\n"
            "6. Выход\n")
        command = input("Выберите пункт меню:")
        while command not in ("1","2","3","4","5","6"):
            print("Некорректный ввод, повторите попытку")
            command = input("Выберите пункт меню:")
        print()
        if command == "1":
            input_data()
        elif command == "2":
            search_contact()
        elif command == "3":
            print_data()
        elif command == "4":
            update_contact()
        elif command == "5":
            delete_contact()
        elif command == "6":
            print("Всего хорошего")

u_interface()
