import requests
import ssl
import socket
from urllib.parse import urlparse


# Ejemplo HTTPS
url_https = "https://www.wikipedia.org"
response_https = requests.get(url_https)
print("HTTPS:", response_https.status_code)
print("Encabezados HTTPS:")
print(response_https.headers)
print("-" * 50)

# Ejemplo HTTP (sin cifrado)
url_http = "http://example.com"  # Sitio HTTP disponible
response_http = requests.get(url_http)
print("HTTP:", response_http.status_code)
print("Encabezados HTTP:")
print(response_http.headers)


# ======================
# 3. Verificación del certificado SSL/TLS
# ======================
# ======================
def verificar_certificado(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    port = 443  # puerto por defecto de HTTPS

    contexto = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with contexto.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()

    print(f"🔐 Certificado de {hostname}:")
    print(" - Emitido por:", cert.get("issuer"))
    print(" - Válido desde:", cert.get("notBefore"))
    print(" - Válido hasta:", cert.get("notAfter"))
    print(" - Nombre común (CN):", cert["subject"][0][0][1])
    print("-" * 50)

# Probar con Wikipedia
verificar_certificado("https://www.wikipedia.org")