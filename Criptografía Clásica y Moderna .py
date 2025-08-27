# =====================================================
# Proyecto: Criptografía Clásica y Moderna en Python
# =====================================================

# ==================
# A. CIFRADO CÉSAR
# ==================
# El Cifrado César desplaza cada letra del alfabeto
# un número fijo de posiciones (la "clave").

def cifrar_cesar(texto, clave):
    """
    Cifra un texto usando el Cifrado César.
    - texto: mensaje original
    - clave: número de posiciones para desplazar
    """
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():  # Solo aplicamos a letras
            # Determinar si la letra es mayúscula o minúscula
            base = ord('A') if caracter.isupper() else ord('a')
            # Convertir letra a número (0-25), aplicar la clave, y volver a letra
            resultado += chr((ord(caracter) - base + clave) % 26 + base)
        else:
            # Mantener espacios, números o signos sin cambios
            resultado += caracter
    return resultado

def descifrar_cesar(texto, clave):
    """
    Descifra un texto usando César.
    Se logra aplicando la clave en negativo.
    """
    return cifrar_cesar(texto, -clave)

def ataque_fuerza_bruta(texto_cifrado):
    """
    Intenta romper un Cifrado César sin conocer la clave.
    Prueba todas las claves posibles (1 a 25) y muestra resultados.
    """
    print("\n--- Ataque de fuerza bruta (César) ---")
    for clave in range(1, 26):
        posible_texto = descifrar_cesar(texto_cifrado, clave)
        print(f"Clave {clave:2d}: {posible_texto}")


# ==================
# B. CIFRADO VIGENÈRE
# ==================
# El Cifrado Vigenère usa una clave alfabética.
# Cada letra del texto se desplaza según la letra de la clave correspondiente.
# Ejemplo: con clave "CLAVE", la primera letra del texto se cifra con "C",
# la segunda con "L", la tercera con "A", etc.

def generar_clave(texto, clave):
    """
    Genera una clave repetida para que tenga el mismo largo que el texto.
    - texto: mensaje a cifrar
    - clave: palabra clave
    """
    clave = list(clave)
    if len(texto) == len(clave):
        return "".join(clave)
    else:
        return "".join([clave[i % len(clave)] for i in range(len(texto))])

def cifrar_vigenere(texto, clave):
    """
    Cifra un texto con el Cifrado Vigenère.
    - texto: mensaje original
    - clave: palabra clave
    """
    resultado = []
    clave_extendida = generar_clave(texto, clave)  # Ajustar clave al tamaño del texto
    for i, c in enumerate(texto):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            base_clave = ord('A') if clave_extendida[i].isupper() else ord('a')
            # Desplazar cada letra usando la letra de la clave
            resultado.append(chr((ord(c) - base + (ord(clave_extendida[i]) - base_clave)) % 26 + base))
        else:
            resultado.append(c)  # Mantener espacios o símbolos
    return "".join(resultado)

def descifrar_vigenere(texto_cifrado, clave):
    """
    Descifra un texto con el Cifrado Vigenère.
    Aplica desplazamientos inversos usando la clave.
    """
    resultado = []
    clave_extendida = generar_clave(texto_cifrado, clave)
    for i, c in enumerate(texto_cifrado):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            base_clave = ord('A') if clave_extendida[i].isupper() else ord('a')
            # Aplicar desplazamiento inverso
            resultado.append(chr((ord(c) - base - (ord(clave_extendida[i]) - base_clave)) % 26 + base))
        else:
            resultado.append(c)
    return "".join(resultado)


# =============================
# C. CIFRADO SIMÉTRICO MODERNO
# =============================
# Se usa la librería "cryptography" con Fernet (basado en AES).
# Este esquema genera una clave segura y cifra mensajes de manera robusta.

from cryptography.fernet import Fernet

# Generar clave segura (se necesita para cifrar y descifrar)
clave_moderna = Fernet.generate_key()
fernet = Fernet(clave_moderna)

def cifrar_moderno(mensaje):
    """
    Cifra un mensaje de texto usando Fernet (AES).
    Retorna el mensaje cifrado en formato bytes.
    """
    return fernet.encrypt(mensaje.encode())

def descifrar_moderno(mensaje_cifrado):
    """
    Descifra un mensaje encriptado con Fernet.
    Retorna el texto original como string.
    """
    return fernet.decrypt(mensaje_cifrado).decode()


# ==================
# PRUEBAS DEL PROYECTO
# ==================
if __name__ == "__main__":
    # ---- Cifrado César ----
    print("\n========== CIFRADO CÉSAR ==========")
    nombre = "Gian Marco"  # Texto de prueba 1
    frase = "La criptografia es divertida"  # Texto de prueba 2
    clave_cesar = 3  # Clave de desplazamiento

    # Probar con el nombre
    cifrado_nombre = cifrar_cesar(nombre, clave_cesar)
    print(f"Nombre original: {nombre}")
    print(f"Nombre cifrado: {cifrado_nombre}")
    print(f"Nombre descifrado: {descifrar_cesar(cifrado_nombre, clave_cesar)}")

    # Probar con la frase
    cifrado_frase = cifrar_cesar(frase, clave_cesar)
    print(f"\nFrase original: {frase}")
    print(f"Frase cifrada: {cifrado_frase}")
    print(f"Frase descifrada: {descifrar_cesar(cifrado_frase, clave_cesar)}")

    # Ataque de fuerza bruta al texto cifrado
    ataque_fuerza_bruta(cifrado_frase)

    # ---- Cifrado Vigenère ----
    print("\n========== CIFRADO VIGENÈRE ==========")
    mensaje = "Seguridad Informatica"  # Mensaje de prueba
    clave_vigenere = "CLAVE"  # Clave de prueba
    mensaje_cifrado = cifrar_vigenere(mensaje, clave_vigenere)
    mensaje_descifrado = descifrar_vigenere(mensaje_cifrado, clave_vigenere)

    print(f"Mensaje original: {mensaje}")
    print(f"Mensaje cifrado (clave '{clave_vigenere}'): {mensaje_cifrado}")
    print(f"Mensaje descifrado: {mensaje_descifrado}")

    # ---- Cifrado Simétrico Moderno ----
    print("\n========== CIFRADO MODERNO (FERNET) ==========")
    mensaje_moderno = "La criptografía moderna es muy segura"
    mensaje_moderno_cifrado = cifrar_moderno(mensaje_moderno)
    mensaje_moderno_descifrado = descifrar_moderno(mensaje_moderno_cifrado)

    print(f"Mensaje original: {mensaje_moderno}")
    print(f"Mensaje cifrado (Fernet): {mensaje_moderno_cifrado}")
    print(f"Mensaje descifrado: {mensaje_moderno_descifrado}")
