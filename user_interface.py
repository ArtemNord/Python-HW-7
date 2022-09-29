
def action_choise():
    print('Добро пожаловать в телефонный справочник!')
    action = input('Что вы хотите сделать?\n1 - Добавить новый контакт\n2 - Вывести на экран список контактов\n')
    print()
    return action   
        
def contact_data_input():
    print("Внесите данные нового контакта")
    first_name = input('Введите имя: ')
    second_name = input('Введите фамилию: ')
    phone_number = input('Введите номер телефона: ')
    data = (first_name, second_name, phone_number)
    print('Контакт успешно добавлен!')
    return data
    