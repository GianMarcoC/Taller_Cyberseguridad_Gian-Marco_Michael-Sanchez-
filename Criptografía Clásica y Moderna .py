# ============================
# Cifrado César en Python
# ============================

# Función para cifrar un texto con César (clave variable)
def cifrar_cesar(texto, clave):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():  # Solo letras
            base = ord('A') if caracter.isupper() else ord('a')
            resultado += chr((ord(caracter) - base + clave) % 26 + base)
        else:
            resultado += caracter  # Mantener espacios y símbolos
    return resultado

# Función para descifrar un texto con César
def descifrar_cesar(texto, clave):
    return cifrar_cesar(texto, -clave)

# Ataque de fuerza bruta: probar todas las claves posibles
def ataque_fuerza_bruta(texto_cifrado):
    print("\n--- Ataque de fuerza bruta ---")
    for clave in range(1, 26):
        posible_texto = descifrar_cesar(texto_cifrado, clave)
        print(f"Clave {clave:2d}: {posible_texto}")


# ============================
# Pruebas
# ============================

# 1. Probar con tu nombre
nombre = "Gian Marco"
clave = 3
cifrado_nombre = cifrar_cesar(nombre, clave)
print(f"Nombre original: {nombre}")
print(f"Nombre cifrado (clave {clave}): {cifrado_nombre}")
print(f"Nombre descifrado: {descifrar_cesar(cifrado_nombre, clave)}\n")

# 2. Probar con una frase
frase = "La criptografia es divertida"
clave = 5
cifrado_frase = cifrar_cesar(frase, clave)
print(f"Frase original: {frase}")
print(f"Frase cifrada (clave {clave}): {cifrado_frase}")
print(f"Frase descifrada: {descifrar_cesar(cifrado_frase, clave)}\n")

# 3. Ataque de fuerza bruta
ataque_fuerza_bruta(cifrado_frase)
