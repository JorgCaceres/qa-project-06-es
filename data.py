# CREAR USUARIO
headers = {
    "Content-Type": "application/json"
}

# CUERPO NUEVO USUARIO
user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

# HEADER CON BEARER AUTHORIZATION
auth_token = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 62bcc59e-54fd-4e1f-9607-17dd0c7cf0d1"
}

# CUERPO CREAR KIT
kit_body = {
    "name": "a"
}