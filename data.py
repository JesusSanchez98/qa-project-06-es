
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {authToken}"
}
user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}
new_client_kit ={
       "name": "Mi conjunto",
       "card": {
           "id": 1,
           "name": "Para la situación"
       },
       "productsList": "null",
       "id": 7,
       "productsCount": 0
   }

#Positive Cases
create_kit_1_letter = "a"
create_kit_511_letters = ("a" * 511)
create_kit_has_special_symbols = ("\"№%@\",")
create_kit_has_space = "A Aaa"
create_kit_has_number = "123"

#Negative Cases
user_empty_name = ""
create_kit_512_letters = ("a" * 512)
create_user_number = 123
