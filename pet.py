class Pet:
    def __init__(self, name: str, age: int, weight: float):
        self.__min_age = 0
        self.__max_age = 55

        is_valid_name = self.__is_valid_name(name)
        is_valid_age = self.__is_valid_age(age)

        if is_valid_name and is_valid_age:
            self.__name = name.title()
            self.__age = age
            self.__weight = weight
        else:
            self.__name = 'Кличка неизвестна'
            self.__age = 0
            self.__weight = 0

    def make_sound(self) -> str:
        return 'молчит'

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def get_weight(self) -> float:
        return self.__weight

    def __is_valid_name(self, name: str) -> bool:
        if isinstance(name, str):
            if name.strip():
                return True

        return False

    def __is_valid_age(self, age: int) -> bool:
        if isinstance(age, int):
            if age > self.__min_age and age <= self.__max_age:
                return True

        return False
