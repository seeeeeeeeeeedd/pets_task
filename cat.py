from pet import Pet


class Cat(Pet):
    def __init__(self, name: str, age: int, weight: float, breed: str):
        super().__init__(name, age, weight)

        is_valid = self.__is_valid_breed(breed)

        if is_valid:
            self.__breed = breed
        else:
            self.__breed = 'Неизвестная порода'

    def make_sound(self) -> str:
        return 'мяу-мяу'

    def get_breed(self) -> str:
        return self.__breed

    def __is_valid_breed(self, breed: str) -> bool:
        if isinstance(breed, str):
            if breed.strip():
                return True

        return False
