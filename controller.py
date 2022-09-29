
from user_interface import action_choise, contact_data_input
from logger import data_logger


def add_new_data():
    data = contact_data_input()
    data_logger(data)


def show_catalog():
    print('Ваш телефонный справочник:')
    with open('catalog.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            print(line)


def click_button():
    action = action_choise()
    if action == '1':
        add_new_data()
    elif action == '2':
        show_catalog()
    else:
        print('Вы выбрали некорректную операцию. Нажмите кнопку еще раз, чтобы начать сначала')
        