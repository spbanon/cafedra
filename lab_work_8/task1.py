class Animal:
    """
    Базовый класс для представления животных.

    Attributes:
        name (str): Имя животного.
        age (int): Возраст животного в годах.

    Methods:
        __init__(self, name: str, age: int) -> None:
            Конструктор класса Animal.

        make_sound(self) -> str:
            Метод, представляющий звук, издаваемый животным.

        sleep(self) -> str:
            Метод, представляющий действие сна животного.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Конструктор класса Animal.

        Parameters:
            name (str): Имя животного.
            age (int): Возраст животного в годах.
        """
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}, {self.age} years old"

    def __repr__(self) -> str:
        return f"Animal(name={self.name}, age={self.age})"

    def make_sound(self) -> str:
        """
        Метод, представляющий звук, издаваемый животным.

        Returns:
            str: Звук, издаваемый животным.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def sleep(self) -> str:
        """
        Метод, представляющий действие сна животного.

        Returns:
            str: Сообщение о сне животного.
        """
        return f"{self.name} is now sleeping."


class Dog(Animal):
    """
    Дочерний класс для представления собак.

    Additional Attributes:
        breed (str): Порода собаки.

    Methods:
        __init__(self, name: str, age: int, breed: str) -> None:
            Конструктор класса Dog.

        make_sound(self) -> str:
            Перегруженный метод, представляющий лай собаки.

        fetch_stick(self) -> str:
            Метод, представляющий действие по подбору палки.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Конструктор класса Dog.

        Parameters:
            name (str): Имя собаки.
            age (int): Возраст собаки в годах.
            breed (str): Порода собаки.
        """
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self) -> str:
        """
        Перегруженный метод, представляющий лай собаки.

        Returns:
            str: Звук лая собаки.
        """
        return "Woof! Woof!"

    def fetch_stick(self) -> str:
        """
        Метод, представляющий действие по подбору палки.

        Returns:
            str: Сообщение о подборе палки.
        """
        return f"{self.name} fetched the stick."

    def sleep(self) -> str:
        """
        Перегруженный метод, представляющий действие сна собаки.

        Returns:
            str: Сообщение о сне собаки.
        """
        return f"{self.name} is sleeping like a dog."
