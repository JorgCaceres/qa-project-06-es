import sender_stand_request
import data


# Función para cambiar el valor del parámetro firstName en el cuerpo de la solicitud
def get_kit_body(name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body


def get_new_user_token():
    new_user = sender_stand_request.post_new_user(data.user_body.copy())
    v_auth_token = new_user.json()['authToken']
    auth_token_test = data.headers.copy()
    auth_token_test["Authorization"] = "Bearer " + v_auth_token
    return auth_token_test


# Función de prueba positiva
def positive_assert(kit_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(kit_name)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())

    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert kit_response.json()["name"] == kit_name


# Función de prueba negativa cuando el error es "No se enviaron todos los parámetros requeridos"
def negative_assert(kit_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(kit_name)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())

    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400

    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert kit_response.json()["code"] == 400


# Prueba 1. Kit creado con éxito. El parámetro name contiene 1 caracter
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert(data.positive_test_1)


# Prueba 2. Kit creado con éxito. El parámetro name contiene 511 caracteres.
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(data.positive_test_2)


# Prueba 3. Error. El parámetro name contiene 1 carácter
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert(data.negative_test_3)


# Prueba 4. Error. El parámetro name contiene 512 carácter
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert(data.negative_test_4)


# Prueba 5. Kit creado con éxito. El parámetro name contiene caracteres especiales
def test_create_kit_special_caracter_in_name_get_success_response():
    positive_assert(data.positive_test_5)


# Prueba 6. Kit creado con éxito. El parámetro name contiene espacios
def test_create_kit_space_caracter_in_name_get_success_response():
    positive_assert(data.positive_test_6)


# Prueba 7. Kit creado con éxito. El parámetro name contiene numeros como string
def test_create_kit_number_caracter_in_name_get_success_response():
    positive_assert(data.positive_test_7)


# Prueba 8. Error. Falta el parámetro name en la solicitud
def test_create_kit_no_parameter_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
    kit_body = data.kit_body.copy()
    # El parámetro "name" se elimina de la solicitud
    kit_body.pop(data.negative_test_8)
    # Comprueba la respuesta
    negative_assert(kit_body)


# Prueba 9. Error. El tipo del parámetro name es Integer
def test_create_kit_number_type_name_get_error_response():
    negative_assert(data.negative_test_4)