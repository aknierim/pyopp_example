class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, l: float) -> None:
        """Initializes a square.

        Parameters
        ----------
        l : float
            Length of the sides of the square.
        """
        super().__init__(self)
        self.length = l

    def area(self) -> float:
        """Computes the area of the square.

        Returns
        -------
        float
            Area of the square.
        """
        return self.length * self.length
