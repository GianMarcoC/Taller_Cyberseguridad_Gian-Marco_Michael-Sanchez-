import requests

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
