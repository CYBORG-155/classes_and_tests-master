from datetime import datetime, timedelta
from typing import Any, Union
from models.user import User
class BloodVolume:
    """
    Specify types of allowed volume of blood to donate
    """
    ONE_DOSE = 450

    CHOICES = (
        ("one_dose", ONE_DOSE),
    )
class Reservation:
    """
    Reservation class which allows to create reservation object
    with user: User, time: datetime and blood_volume: BloodVolume.CHOICES
    """
    user: User
    time: datetime
    blood_volume: BloodVolume.CHOICES
    def __init__(self, user: User, time: datetime, blood_volume: BloodVolume.CHOICES):
        self.user = self._is_valid_user(user)
        self.time = self._is_valid_time(time)
        self.blood_volume = self._is_valid_blood_volume(blood_volume)
    def _is_valid_user(self, user: Union[User, Any]) -> User:
        """
        Validator checks for correct user type
        :param user:
        :return:
        """
        if not isinstance(user, User):
            raise ValueError("Wrong user object")
        return user
    def _is_valid_time(self, time: datetime) -> datetime:
        """
        Validator checks for correct datetime type and
        allows only date in future
        :param time:
        :return:
        """
        if not isinstance(time, datetime):
            raise ValueError("Wrong date object")
        if not time > datetime.now():
            raise ValueError("Enter date in future")
        return time
    def _is_valid_blood_volume(self, blood_volume):
        """
        Validator checks for allowed blood volume
        :param blood_volume:
        :return:
        """
        for _, value in BloodVolume.CHOICES:
            if blood_volume == value:
                return blood_volume
        raise ValueError("Enter correct blood volume")
    def __str__(self):
        return (
            f"Reservation for user {self.user.first_name} at {self.time} for {self.blood_volume} ml"
        )
