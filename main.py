from dog import Dog
from cat import Cat

INVALID_AGE = 0
INVALID_WEIGHT = INVALID_AGE

DECIMAL_SEPARATOR_SYMBOL = '.'
EMPTY_REPLACEMENT = ''
MAX_REPLACEMENTS_COUNT = 1

UNKNOWN_COMMAND_MESSAGE = 'Неизвестная команда. Попробуйте снова'

commands = {
    '1': 'Добавить собаку',
    '2': 'Добавить кошку',
    '3': 'Показать всех питомцев',
    '0': 'Выйти из программы'
}

ADD_DOG_COMMAND, ADD_CAT_COMMAND, SHOW_ALL_COMMAND, EXIT_COMMAND = commands.keys()

pets = []


def print_commands():
    for number, command in commands.items():
        print(f'{number}: {command}')


def get_pet_data():
    name = input('Укажите кличку: ').strip()
    age = input('Укажите возраст: ').strip()
    weight = input('Укажите вес: ').strip()

    if not is_valid_age(age):
        print('Возраст должен быть числом')
        age = INVALID_AGE
    else:
        age = int(age)

    if not is_valid_weight(weight):
        print('Вес должен быть числом')
        weight = INVALID_WEIGHT
    else:
        weight = float(weight)

    return name, age, weight


def is_valid_age(age: str) -> bool:
    if not isinstance(age, str):
        return False

    return age.isdigit()


def is_valid_weight(weight: str) -> bool:
    if not isinstance(weight, str):
        return False

    return weight.replace(DECIMAL_SEPARATOR_SYMBOL, EMPTY_REPLACEMENT, MAX_REPLACEMENTS_COUNT).isdigit()


def show_all_pets():
    if not pets:
        print('Список питомцев пуст')
    else:
        for pet in pets:
            print(pet.print_info())


is_program_running = True

while is_program_running:
    print_commands()
    user_command_number = input('Укажите номер команды: ').strip()

    if user_command_number in commands:
        if user_command_number == ADD_DOG_COMMAND:
            name, age, weight = get_pet_data()
            breed = input('Укажите породу: ').strip()
            user_dog = Dog(name, age, weight, breed)
            pets.append(user_dog)
        elif user_command_number == ADD_CAT_COMMAND:
            name, age, weight = get_pet_data()
            breed = input('Укажите породу: ').strip()
            user_cat = Cat(name, age, weight, breed)
            pets.append(user_cat)
        elif user_command_number == SHOW_ALL_COMMAND:
            show_all_pets()
        elif user_command_number == EXIT_COMMAND:
            print('Выход из программы')
            is_program_running = False
        else:
            print(UNKNOWN_COMMAND_MESSAGE)
    else:
        print(UNKNOWN_COMMAND_MESSAGE)
