# ============================
# Firma Digital
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