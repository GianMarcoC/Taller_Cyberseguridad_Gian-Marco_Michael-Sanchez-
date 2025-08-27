import hashlib
import hmac
import os

# =============================
# FUNCIONES HASH (SHA-256)
# =============================

def hash_text(text):
    """
    Calcula el hash SHA-256 de un texto.
    """
    return hashlib.sha256(text.encode()).hexdigest()

def hash_file(filename):
    """
    Calcula el hash SHA-256 de un archivo.
    Lee el archivo en bloques para no cargarlo todo en memoria.
    """
    sha256 = hashlib.sha256()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):  # Lee en bloques de 4 KB
            sha256.update(block)
    return sha256.hexdigest()


# =============================
# DETECCIÓN DE INTEGRIDAD
# =============================

def compare_files(file1, file2):
    """
    Compara los hashes SHA-256 de dos archivos.
    Retorna True si son idénticos, False en caso contrario.
    """
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)
    hash3 = hash_file(file3)
    return hash1 == hash2 == hash3


# =============================
# HMAC con SHA-256
# =============================

def generate_hmac(message, key):
    """
    Genera un HMAC-SHA256 a partir de un mensaje y una clave.
    """
    return hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()

def verify_hmac(message, key, hmac_to_verify):
    """
    Verifica si un HMAC recibido coincide con el generado.
    """
    expected_hmac = generate_hmac(message, key)
    return hmac.compare_digest(expected_hmac, hmac_to_verify)


# =============================
# AUTENTICACIÓN CON HASH + SAL
# =============================

def register_user(password):
    """
    Simula el registro de un usuario:
    - Genera una sal aleatoria (16 bytes)
    - Calcula hash de la contraseña + sal
    - Retorna sal y hash para guardar en la base de datos
    """
    salt = os.urandom(16).hex()  # Se guarda como string hexadecimal
    salted_pass = password + salt
    hashed_pass = hashlib.sha256(salted_pass.encode()).hexdigest()
    return salt, hashed_pass

def login_user(password, salt, stored_hash):
    """
    Simula el inicio de sesión:
    - Usa la misma sal que se generó en el registro
    - Recalcula el hash y lo compara con el guardado
    """
    salted_pass = password + salt
    hashed_pass = hashlib.sha256(salted_pass.encode()).hexdigest()
    return hashed_pass == stored_hash


# =============================
# Pruebas
# =============================
if __name__ == "__main__":

    print("\n===== HASH DE TEXTO =====")
    text1 = "Hola mundo"
    text2 = "Hola mundo!"
    print("Texto 1:", hash_text(text1))
    print("Texto 2:", hash_text(text2))
    print("Nota: aunque el texto cambie poco, el hash cambia por completo.\n")

    print("===== HASH DE ARCHIVOS =====")
    #Para probar esto se creo 2 archivos de texto:
    # archivo1.txt con "Hola mundo"
    # archivo2.txt con "Hola mundo!"
    # Se crea un archivo3 con un mensaje correcto para la comprobacion
    file1 = "archivo1.txt"
    file2 = "archivo2.txt"
    file3 = "archivo3.txt "
    print(f"Hash {file1}: {hash_file(file1)}")
    print(f"Hash {file2}: {hash_file(file2)}")
    print(f"Hash {file3}: {hash_file(file3)}")

    print("\n¿Los archivos son idénticos?:", compare_files(file1, file2))
    print("\nAhora se comprueba con un mensaje correcto")
    print("\n¿Los archivos son idénticos?:", compare_files(file1, file3))
    print("\n===== HMAC =====")
    key = "clave_secreta"
    msg = "Mensaje importante"
    hmac_value = generate_hmac(msg, key)
    print("HMAC generado:", hmac_value)
    print("Verificación correcta:", verify_hmac(msg, key, hmac_value))
    print("Se verifica ahora con otra_clave")
    print("Verificación incorrecta:", verify_hmac(msg, "otra_clave", hmac_value))

    print("\n===== AUTENTICACIÓN CON SAL =====")
    # Registro
    user_password = "123456"
    salt, stored_hash = register_user(user_password)
    print("Sal guardada:", salt)
    print("Hash guardado:", stored_hash)

    # Inicio de sesión correcto
    print("Inicio de sesión (correcto):", login_user("123456", salt, stored_hash))
    print("Se prueba ahora con otro mensaje distinto")
    # Inicio de sesión incorrecto
    print("Inicio de sesión (incorrecto):", login_user("password_mal", salt, stored_hash))
