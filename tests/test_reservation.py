from datetime import datetime, timedelta
import pytest
from models.reservation import Reservation
def test_reservation_ok(user):
	time = datetime.now() + timedelta(days=10)
	reservation = Reservation(user, time, 450)
	assert str(reservation) == f"Reservation for user first_name at {str(time)} for 450 ml"
def test_reservation_time_in_past(user):
	time_in_past = datetime.now() - timedelta(days=10)
	with pytest.raises(ValueError) as error:
		Reservation(user, time_in_past, 450)
	assert str(error.value) == "Enter date in future"
def test_reservation_wrong_time_type(user):
	time = "wrong type"
	with pytest.raises(ValueError) as error:
		Reservation(user, time, 450)
	assert str(error.value) == "Wrong date object"
def test_reservation_wrong_user_type():
	time = datetime.now() + timedelta(days=10)
	user = "wrong type"
	with pytest.raises(ValueError) as error:
		Reservation(user, time, 450)
	assert str(error.value) == "Wrong user object"
def test_reservation_wrong_blood_volume(user):
	time = datetime.now() + timedelta(days=10)
	with pytest.raises(ValueError) as error:
		Reservation(user, time, 750)

	assert str(error.value) == "Enter correct blood volume"
