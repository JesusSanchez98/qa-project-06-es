
import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def token_generation():
    respuesta = post_new_user(data.user_body)
    dato = respuesta.json()
    return dato ['authToken']


def post_new_client_kit(client_kit):
    Token = token_generation()
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {Token}"

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT,
                         json=client_kit,
                         headers=data.headers,
                         )

