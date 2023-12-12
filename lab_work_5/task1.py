import doctest


class Square:
    def __init__(self, height: float, width: float):
        """
        Создание и подготовка к работе объекта "Прямоугольник"

        :param height: Длина прямоугольника
        :param width: Ширина прямоугольника 

        Примеры:
        >>> square = Square(500,500)  # инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Длина должна быть типа int или float")
        if height < 0:
            raise ValueError("Длина не может быть отрицательным числом")
        self.height = height

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина должна быть int или float")
        if width < 0:
            raise ValueError("Ширина не может быть отрицательным числом")
        self.occupied_volume = width

    def is_square_visible(self) -> bool:
        """
        Функция которая проверяет является ли прямоугольник видимым

        :return: Является ли  является ли прямоугольник видимым

        Примеры:
        >>> square = Square(500, 500)
        >>> square.is_square_visible()
        """
        ...

    def change_color(self, color: float) -> None:
        """
        Изменение цвета прямоугольника
        :param color: новый цвет

        :raise ValueError: Если цвет < 0 , то вызываем ошибку

        Примеры:
        >>> square = Square(500, 500)
        >>> square.change_color(200)
        """
        if not isinstance(color, (int, float)):
            raise TypeError("цвет должнаен быть типа int или float")
        if color < 0:
            raise ValueError("цвет должнен быть положительным числом")
        
        ...
    def remove_square(self) -> None:
        """
        Удаление квадрата

        Примеры:
        >>> square = Square(500, 500)
        >>> square.remove_square()
        """
        ...



class Circle:
    def __init__(self, radius: float, color: float):
        """
        Создание и подготовка к работе объекта "Прямоугольник"

        :param radius: радиус круга
        :param color: цвет круга

        Примеры:
        >>> circle = Circle(500,500)  # инициализация экземпляра класса
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус должнен быть типа int или float")
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным числом")
        self.radius = radius

        if not isinstance(color, (int, float)):
            raise TypeError("Цвет должнен быть int или float")
        if color < 0:
            raise ValueError("Цвет не может быть отрицательным числом")
        self.color = color

    def is_circle_visible(self) -> bool:
        """
        Функция которая проверяет является ли круг видимым

        :return: Является ли  является ли круг видимым

        Примеры:
        >>> circle = Circle(500, 500)
        >>> circle.is_circle_visible()
        """
        ...

    def change_color(self, color: float) -> None:
        """
        Изменение цвета круга
        :param color: новый цвет

        :raise ValueError: Если цвет < 0 , то вызываем ошибку

        Примеры:
        >>> circle = Circle(500, 500)
        >>> circle.change_color(200)
        """
        if not isinstance(color, (int, float)):
            raise TypeError("цвет должнаен быть типа int или float")
        if color < 0:
            raise ValueError("цвет должнен быть положительным числом")
        
        ...
    def remove_circle(self) -> None:
        """
        Удаление круга

        Примеры:
        >>> circle = Circle(500, 500)
        >>> circle.remove_circle()
        """
        ...

class Line:
    def __init__(self, length: float, color: float):
        """
        Создание и подготовка к работе объекта "Прямоугольник"

        :param length: длина линии
        :param color: цвет линии

        Примеры:
        >>> line = Line(500,500)  # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина должна быть типа int или float")
        if length < 0:
            raise ValueError("Длина не может быть отрицательным числом")
        self.length = length

        if not isinstance(color, (int, float)):
            raise TypeError("Цвет должнен быть int или float")
        if color < 0:
            raise ValueError("Цвет не может быть отрицательным числом")
        self.color = color

    def is_line_visible(self) -> bool:
        """
        Функция которая проверяет является ли линия видимой

        :return: Является ли  является ли линия видимой

        Примеры:
        >>> line = Line(500, 500)
        >>> line.is_line_visible()
        """
        ...

    def change_color(self, color: float) -> None:
        """
        Изменение цвета линии
        :param color: новый цвет

        :raise ValueError: Если цвет < 0 , то вызываем ошибку

        Примеры:
        >>> line = Line(500, 500)
        >>> line.change_color(200)
        """
        if not isinstance(color, (int, float)):
            raise TypeError("цвет должнаен быть типа int или float")
        if color < 0:
            raise ValueError("цвет должнен быть положительным числом")
        
        ...
    def remove_line(self) -> None:
        """
        Удаление линии

        Примеры:
        >>> line = Line(500, 500)
        >>> line.remove_line()
        """
        ...     
        
        
        
        
        
        
if __name__ == "__main__":
    doctest.testmod()  