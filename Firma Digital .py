# ============================
# Firma Digital
# ============================
# Objetivo: Comprender cómo se genera y verifica una firma digital.

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# ============================
# 1. Generar par de claves RSA
# ============================
# - La clave privada sirve para firmar mensajes.
# - La clave pública sirve para verificar la firma.
private_key = rsa.generate_private_key(
    public_exponent=65537,  # Valor recomendado para RSA (seguro y eficiente)
    key_size=2048           # Tamaño de la clave en bits (2048 es seguro actualmente)
)
public_key = private_key.public_key()

# ============================
# 2. Mensaje original
# ============================
mensaje = b"Este es un mensaje importante"

# ============================
# 3. Crear firma con la clave privada
# ============================
# - La firma se genera con la clave privada.
# - Se usa el algoritmo RSA-PSS con SHA-256.
firma = private_key.sign(
    mensaje,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("Firma generada (hex):", firma.hex(), "\n")

# ============================
# 4. Verificar firma con la clave pública
# ============================
# - Si el mensaje no ha cambiado, la verificación será correcta.
print("Verificando mensaje original...")
try:
    public_key.verify(
        firma,
        mensaje,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("✅ La firma es válida (mensaje íntegro).")
except:
    print("❌ La firma no es válida.")

# ============================
# 5. Probar con un mensaje modificado
# ============================
# - Si el mensaje cambia aunque sea un carácter, la firma dejará de ser válida.
mensaje_modificado = b"Este es un mensaje alterado"

print("\nVerificando mensaje modificado...")
try:
    public_key.verify(
        firma,
        mensaje_modificado,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("✅ La firma es válida (mensaje íntegro).")
except:
    print("❌ La firma no es válida (mensaje fue modificado).")