import data
import sender_stand_request

def get_new_client_kit(the_name):
    current_body = data.new_client_kit.copy()
    current_body["name"] = the_name
    return current_body

def positive_assert(the_name):
    user_body = get_new_client_kit(the_name)
    user_response = sender_stand_request.post_new_client_kit(user_body)

    assert user_response.status_code == 201

def test_create_kit_1_letter__name_get_success_response():
    positive_assert("a")
def test_create_kit_511_letters_in_name_get_success_response():
    positive_assert("a" * 512)
def test_create_kit_has_special_symbols_in_name_get_success_response():
    positive_assert("\"№%@\",")
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert("A Aaa")
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert("123")

def negative_assert_no_firstname(the_name):
    response = sender_stand_request.post_new_client_kit(the_name)

    assert response.status_code == 400
    assert response.json()["code"] == 400

def test_create_user_empty_first_name_get_error_response():
    user_body = get_new_client_kit("")
    negative_assert_no_firstname(user_body)

def test_create_kit_512_letters_in_name_get_error_response():
    user_body = get_new_client_kit("a" * 512)
    negative_assert_no_firstname(user_body)

def test_create_kit_no_name_get_error_response():
    user_body = data.new_client_kit.copy()
    user_body.pop("name")
    negative_assert_no_firstname(user_body)

def test_create_user_number_type_first_name_get_error_response():
    user_body = get_new_client_kit(123)
    negative_assert_no_firstname(user_body)
def test_create_user_number_type_first_name_get_error_response():
    user_body = get_new_client_kit(12)
    negative_assert_no_firstname(user_body)

