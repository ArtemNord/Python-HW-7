
def data_logger(data):
    first_name, second_name, phone_number = data
    with open('catalog.txt', 'a+', encoding='UTF-8') as file:
        file.write(f'{second_name} {first_name} тел. {phone_number}\n')
        