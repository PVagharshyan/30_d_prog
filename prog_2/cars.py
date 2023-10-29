class Utility:
    @staticmethod
    def check_make(make: str) -> bool:
        if not isinstance(make, str):
            raise MakeNotValidError("...")
        return True

    @staticmethod
    def check_model(model: str) -> bool:
        if not isinstance(model, str):
            raise ModelNotValidError("...")
        return True

    @staticmethod
    def check_price(price: (float, int)) -> bool:
        if not isinstance(price, (float, int)):
            raise PriceNotValidError("...")
        return True


class Car:
    def __init__(self, make: str, model: str, price: (float, int)) -> None:
        self.make = make
        self.model = model
        self.price = price

    def __str__(self):
        return f"make: {self.make}, model: {self.model}, price: {self.price}$"

    def __eq__(self, other) -> bool:
        return (
            self.make == other.make and
            self.model == other.model and
            self.price == other.price
        )

    @property
    def make(self) -> str:
        return self._make

    @make.setter
    def make(self, new_make: str) -> str:
        Utility.check_make(new_make)
        self._make = new_make

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, new_model: str) -> None:
        Utility.check_model(new_model)
        self._model = new_model

    @property
    def price(self) -> (float, int):
        return self._price

    @price.setter
    def price(self, new_price: (float, int)) -> None:
        Utility.check_price(new_price)
        self._price = new_price

def main():
    c = Car("ddd", "bbb", 25)
    print(c)

if __name__ == "__main__":
    main()

