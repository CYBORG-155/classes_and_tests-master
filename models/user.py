class User:
    """
    User class responsible for creating User instance with arguments below
    :param first_name:
    :param last_name:
    :param phone_number:
    :param age:
    """
    first_name: str
    last_name: str
    phone_number: int
    age: int

    def __init__(self, first_name: str, last_name: str, phone_number: int, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = self._is_valid_phone_number(phone_number)
        self.age = self._is_valid_age(age)

    def _is_valid_phone_number(self, phone_number: int) -> int:
        """
        Validator checks for correct length of phone number
        :param phone_number:
        :return:
        """
        if len(str(phone_number)) != 9:
            raise ValueError("Enter correct phone number")
        return phone_number

    def _is_valid_age(self, age: int) -> int:
        """
        Validator checks for mature age to donate blood
        :param age:
        :return:
        """
        if age < 18 or age>65 :
            raise ValueError("You can't donate blood because of age")
        return age

    def __str__(self) -> str:
        return f"User: {self.first_name} {self.last_name}, {self.age} years old"
