from datetime import date
from random import choice
from faker import Faker
from transliterate import translit

faker = Faker('ru_RU')

#вычисляет возраст, отталкиваясь от текущей даты и даты, которую сгенерирует в качестве даты рождения библиотека фейкера
def calculate_age():
    today = date.today()
    year_f = int(str(faker.date_of_birth(minimum_age=15, maximum_age=60)).split("-")[0])
    month_f = int(str(faker.date_of_birth(minimum_age=15, maximum_age=60)).split("-")[1])
    day_f = int(str(faker.date_of_birth(minimum_age=15, maximum_age=60)).split("-")[2])
    age_t = today.year - year_f - ((today.month, today.day) < (month_f, day_f))
    bith_date = f'{day_f}.{month_f}.{year_f}'
    return age_t, bith_date

#Здесь получаем Ф.И.О, дату рождения, возраст, место работы, должность и еще несколько плюшек. Затем заполненный словарь возвращаем из функции
def faker_person_create():

    age, b_date = calculate_age()
    credit_card = f'{faker.credit_card_number()}, Срок действия: {faker.credit_card_expire()}, ' \
                  f'CVS-код: {faker.credit_card_security_code()}'
    dict_mail = ['@mail.ru', '@yandex.ru', '@rambler.ru', '@gmail.com', '@bk.ru']
    name_f = faker.name()
    vk_ur = f'{str(name_f).split()[0].lower()}_{str(name_f).split()[2][:4].lower()}'
    dict_person = {'Ф.И.О.': name_f, 'Дата рождения': b_date, 'Возраст': age, 'Место работы': faker.company(),
                   'Должность': faker.job().lower(), 'Адрес': f'Россия, {faker.address()[0:-8]}',
                   'Почтовый индекс': faker.address()[-6:], 'Телефон': faker.phone_number(),
                   'E-mail': translit(str(name_f).split()[0].lower(), language_code='ru', reversed=True) + \
                             choice(dict_mail),
                   'Профиль VK': "https://vk.com/" + translit(vk_ur, language_code='ru', reversed=True). \
                       replace("'", "").replace(".", ""),
                   'Банковская карта': credit_card}

    return dict_person

#Затем создаем функцию печати, print_person_data(dict_person, i), которая принимает сгенерированный словарь с данными, а также порядковый номер сгенерированных данных. После чего в цикле распечатывается и сохраняется в текстовый файл
def print_person_data(dict_person, i):
    with open('person_faker.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{"-" * 16} {i + 1} {"-" * 16}\n')
    for item in dict_person:
        print(f'{item}: {dict_person[item]}')
        with open('person_faker.txt', 'a', encoding='utf-8') as file:
            file.write(f'{item}: {dict_person[item]}\n')

#Здесь понятно
def main():
    person_count = str(input('\n[+] Сколько личностей вы хотите сгенерировать >>> '))
    for i in range(person_count):
        print(f'\n{"-" * 16} {i + 1} {"-" * 16}\n')
        dict_person = faker_person_create()
        print_person_data(dict_person, i)

if __name__ == "__main__":

    main()


