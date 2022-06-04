import pytest

from models.user import User


def test_user_model_ok():
	user = User("first", "last", 123456789, 18)
	
	assert isinstance(user, User)
	assert str(user) == "User: first last, 18 years old"


def test_user_model_wrong_phone_number():
	with pytest.raises(ValueError) as error:
		User("first", "last", 12345678, 18)
	assert str(error.value) == "Enter correct phone number"


def test_user_model_young_age():
	with pytest.raises(ValueError) as error:
		User("first", "last", 123456789, 17)
	assert str(error.value) == "You can't donate blood because of age"

def test_user_model_old_age():
	with pytest.raises(ValueError) as error:
		User("first", "last", 123456789, 66)
	assert str(error.value) == "You can't donate blood because of age"
